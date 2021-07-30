import uvicorn


if __name__ == '__main__':
    uvicorn.run(
        'source.application:application',
        host='0.0.0.0',
        port=4000,
        reload=True,
    )
