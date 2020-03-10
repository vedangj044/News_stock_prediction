function useFetch(url, options){
    const [response, setResponse] = React.useState(null);
    const [error, setError] = React.useState(null);
    React.useEffect(() => {
      const fetchData = async () => {
        try {
          const res = await fetch(url, options);
          const json = await res.json();
          setResponse(json);
        } catch (error) {
          setError(error);
        }
      };
      fetchData();
    }, []);
    return { response, error };
  };

  function getDataXHR(url) {
    var xhr = new XMLHttpRequest()
    xhr.addEventListener('load', () => {
      console.log(xhr.responseText)
    })
    xhr.open('GET', url)
    xhr.send()
  }

  function getDataXHR(url, param) {
    var xhr = new XMLHttpRequest()
    xhr.addEventListener('load', () => {
      console.log(xhr.responseText)
    })
    xhr.open('POST', url)
    // xhr.send(JSON.stringify({ example: 'data' }))
    xhr.send(JSON.stringify(param))
  }

  async function getDataAxios(url){
    const response =
      await axios.get(url)
    console.log(response.data)
    return response
}