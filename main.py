import uvicorn


if __name__ == '__main__':
    uvicorn.run(
        'source.application:application',
        host='127.0.0.1',
        port=4000,
        reload=True,
    )
