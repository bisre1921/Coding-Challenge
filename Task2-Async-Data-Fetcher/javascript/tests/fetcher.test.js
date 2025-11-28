const { fetchWithRetry } = require('../src/fetcher');

// Mock global fetch
global.fetch = jest.fn();

describe('fetchWithRetry', () => {
    beforeEach(() => {
        fetch.mockClear();
    });

    test('should return data on successful fetch', async () => {
        const mockData = { id: 1, title: 'Test Todo' };
        fetch.mockResolvedValueOnce({
            ok: true,
            json: async () => mockData
        });

        const data = await fetchWithRetry('https://api.example.com/data');
        expect(data).toEqual(mockData);
        expect(fetch).toHaveBeenCalledTimes(1);
    });

    test('should retry on failure and eventually succeed', async () => {
        const mockData = { id: 1, title: 'Retry Success' };

        // Fail twice, then succeed
        fetch
            .mockResolvedValueOnce({ ok: false, status: 500 })
            .mockRejectedValueOnce(new Error('Network Error'))
            .mockResolvedValueOnce({
                ok: true,
                json: async () => mockData
            });

        const data = await fetchWithRetry('https://api.example.com/data', 3, 10);

        expect(data).toEqual(mockData);
        expect(fetch).toHaveBeenCalledTimes(3);
    });

    test('should throw error after max retries exhausted', async () => {
        fetch.mockRejectedValue(new Error('Persistent Network Error'));

        await expect(fetchWithRetry('https://api.example.com/data', 2, 10))
            .rejects
            .toThrow('Failed to fetch after 2 retries');

        expect(fetch).toHaveBeenCalledTimes(3); // Initial + 2 retries
    });

    test('should handle HTTP errors as failures', async () => {
        fetch.mockResolvedValue({
            ok: false,
            status: 404
        });

        await expect(fetchWithRetry('https://api.example.com/404', 1, 10))
            .rejects
            .toThrow('HTTP error! status: 404');

        expect(fetch).toHaveBeenCalledTimes(2);
    });
});
