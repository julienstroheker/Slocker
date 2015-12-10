# Slocker - Hook from DockerHub to Slack in a container

## Installation and Usage

Create a DockerFile like :

1. `FROM julienstroheker/slocker`
2. `ENV Slack_Hook_Url 'https://hooks.slack.com/services/XXXXX/XXXXXX/XXXXXXXXXX'`
3. `COPY app/redirectChannel.json /usr/src/app/redirectChannel.json`
4. `EXPOSE 8080`
5. `CMD python2 /usr/src/app/slocker.py`

Build your container `Docker Build DockerFile`

You'll need to modfify the redirectChannel.json with your own parameters :

```{
"NameUserDocker/NameRepoDocker":"#YourSlackChannel"
}```

Execute your container `Docker run -d -p 8080:8080 julienstroheker/slocker`

Enjoy

## Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D

## History

v1.0 - Julien Stroheker
