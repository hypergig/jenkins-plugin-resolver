# Jenkins Plugin Resolver #
Handy python thing that wraps up resolving Jenkins plugin dependencies via the Jenkins Update Center. To be used with the [Jenkins docker plugins.sh script](https://github.com/jenkinsci/docker/blob/master/plugins.sh) to automate dependency resolution. Related to [issue 147](https://github.com/jenkinsci/docker/issues/147).

# GOOD NEWS! #
Jenkins has finally incorperated plugin dependency resolution into their docker image!
https://github.com/jenkinsci/docker/tree/master#preinstalling-plugins

# How to use it #
* Import the module
```
>>> 
>>> from JenkinsPluginResolver.JenkinsPluginResolver import JenkinsPluginResolver
>>> 
```
* Instantiation
```
>>> 
>>> jpr = JenkinsPluginResolver()
>>> 
```
* Lets `dump` the plugin dict
```
>>> 
>>> jpr.dump()
{}
>>>
```
* Oh, it's empty, lets `load` the github plugin, that sucker has lots of dependences
```
>>>  
>>> jpr.load('github')
>>> 
```
* Now lets see the plugin dict
```
>>> 
>>> pprint(jpr.dump())
{u'conditional-buildstep': 'latest',
 u'credentials': 'latest',
 u'git': 'latest',
 u'git-client': 'latest',
 'github': 'latest',
 u'github-api': 'latest',
 u'icon-shim': 'latest',
 u'javadoc': 'latest',
 u'junit': 'latest',
 u'mailer': 'latest',
 u'mapdb-api': 'latest',
 u'matrix-project': 'latest',
 u'maven-plugin': 'latest',
 u'parameterized-trigger': 'latest',
 u'plain-credentials': 'latest',
 u'project-inheritance': 'latest',
 u'promoted-builds': 'latest',
 u'rebuild': 'latest',
 u'run-condition': 'latest',
 u'scm-api': 'latest',
 u'script-security': 'latest',
 u'ssh-credentials': 'latest',
 u'subversion': 'latest',
 u'token-macro': 'latest'}
>>> 
```
* The latest `maven-plugin` has given me trouble in the past, lets pin that
```
>>> 
>>> jpr.load('maven-plugin','2.12.1')
>>> pprint(jpr.dump())
{u'conditional-buildstep': 'latest',
 u'credentials': 'latest',
 u'git': 'latest',
 u'git-client': 'latest',
 'github': 'latest',
 u'github-api': 'latest',
 u'icon-shim': 'latest',
 u'javadoc': 'latest',
 u'junit': 'latest',
 u'mailer': 'latest',
 u'mapdb-api': 'latest',
 u'matrix-project': 'latest',
 u'maven-plugin': '2.12.1',
 u'parameterized-trigger': 'latest',
 u'plain-credentials': 'latest',
 u'project-inheritance': 'latest',
 u'promoted-builds': 'latest',
 u'rebuild': 'latest',
 u'run-condition': 'latest',
 u'scm-api': 'latest',
 u'script-security': 'latest',
 u'ssh-credentials': 'latest',
 u'subversion': 'latest',
 u'token-macro': 'latest'}
>>> 
```
* Great! But I don't really need all that so lets clear it.
```
>>> 
>>> jpr.clear()
>>> jpr.dump()
{}
>>> 
```
* Wondering what the actual [Update Center post](https://updates.jenkins-ci.org/current/update-center.json) looks like (why?), well you can
```
>>> 
>>> jpr.uc_post()
{
# a very large block of text that has no place in a readme
}
>>> 
```

# Methods #
| Method                    | Purpose                                     | Returns |
|---------------------------|---------------------------------------------|---------|
| `load(plugin[, version])` | Add and resolve plugins, latest by default  |         |
| `dump()`                  | Dump the current plugin list                | `dict`  |
| `clear()`                 | Blows out the current plugins `dict`        |         |
| `uc_post()`               | If you need to see the Update Center post   | `dict`  |

# Gotcha #
Since the Update Center post only lists the latest version of each plugin, the latest version of dependencies is all that can be automatically resolved. But you can always override a version by pinning it with `load` if there is a conflict or issue.

# Further Development #
PRs are always welcomed. Please test the code before submitting.
```
16:12 $ nosetests
..........
----------------------------------------------------------------------
Ran 10 tests in 0.029s

OK
16:13 $ 
```

# Coming soon #
* Integration and examples with the [Jenkins docker plugins.sh script](https://github.com/jenkinsci/docker/blob/master/plugins.sh)
* Formal PR replacing the `plugins.sh` process in [Jenkins Docker](https://github.com/jenkinsci/docker) *fingers crossed*

