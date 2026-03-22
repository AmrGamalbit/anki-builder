const baseUrl = import.meta.env.VITE_API_URL
const endpointMap = {
  dictionary: 'lookup',
  ai: 'generate',
};

const payloads = {
    dictionary: ['content', 'target_language', 'include_pronunciation', 'use_dictionary_audio', 'provider'],
    ai: ['content', 'mode', 'source_language', 'target_language', 'include_pronunciation', 'provider'],
}

function pick(obj, keys) {
    return keys.reduce((acc, key) => {
        if (key in obj) acc[key] = obj[key]
        return acc
    }, {})
}

export function useApi() {
    function getEndpoint(source, type) {
        let endpoint = `${baseUrl}/${source}/${endpointMap[source]}`
        if (type == 'file') {
            endpoint += '/upload'
        }
        return endpoint
    }

    function buildPayload(data, type) {
        const payload = pick(data, payloads[data.source])
        if (type === 'file') {
            const formData = new FormData();
            for (const key in payload) {
                formData.append(key, payload[key])
            }
            return formData
        }
        return payload
    }
    return { getEndpoint, buildPayload }
}