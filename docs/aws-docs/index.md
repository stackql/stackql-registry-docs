---
title: aws
hide_title: false
hide_table_of_contents: false
keywords:
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
id: aws-doc
slug: /providers/aws

---
Cloud services from AWS.

:::info Provider Summary (v23.11.00181)

<div class="row">
<div class="providerDocColumn">
<span>total services:&nbsp;<b>214</b></span><br />
<span>total methods:&nbsp;<b>2,612</b></span><br />
</div>
<div class="providerDocColumn">
<span>total resources:&nbsp;<b>2,178</b></span><br />
<span>total selectable resources:&nbsp;<b>2,082</b></span><br />
</div>
</div>

:::

See also:   
[[` SHOW `]](https://stackql.io/docs/language-spec/show) [[` DESCRIBE `]](https://stackql.io/docs/language-spec/describe)  [[` REGISTRY `]](https://stackql.io/docs/language-spec/registry)
* * * 

## Installation

To pull the latest version of the `aws` provider, run the following command:  

```bash
REGISTRY PULL aws;
```
> To view previous provider versions or to pull a specific provider version, see [here](https://stackql.io/docs/language-spec/registry).  

## Authentication

The following system environment variables are used for authentication by default:  

- `AWS_ACCESS_KEY_ID` - AWS Access Key ID (see [How to Create AWS Credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html))
- `AWS_SECRET_ACCESS_KEY` - AWS Secret Access Key (see [How to Create AWS Credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html))
- `AWS_SESSION_TOKEN` - [__OPTIONAL:__ only required if using `aws sts assume-role`] AWS Session Token (see [Temporary security credentials in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html))
  
These variables are sourced at runtime (from the local machine or as CI variables/secrets).  

<details>

<summary>Using different environment variables</summary>

To use different environment variables (instead of the defaults), use the `--auth` flag of the `stackql` program.  For example:  

```bash

AUTH='{ "aws": { "type": "aws_signing_v4", "keyIDenvvar": "YOUR_ACCESS_KEY_ID_VAR", "credentialsenvvar": "YOUR_SECRET_KEY_VAR" }}'
stackql shell --auth="${AUTH}"

```
or using PowerShell:  

```powershell

$Auth = "{ 'aws': { 'type': 'aws_signing_v4',  'keyIDenvvar': 'YOUR_ACCESS_KEY_ID_VAR', 'credentialsenvvar': 'YOUR_SECRET_KEY_VAR' }}"
stackql.exe shell --auth=$Auth

```
</details>


## Server Parameters


The following parameter is required for the `aws` provider:  

- `region` - AWS region (e.g. `us-east-1`)

This parameter must be supplied to the `WHERE` clause of each `SELECT` statement.

## Services
<div class="row">
<div class="providerDocColumn">
<a href="/providers/aws/accessanalyzer/">accessanalyzer</a><br />
<a href="/providers/aws/acmpca/">acmpca</a><br />
<a href="/providers/aws/amazonmq/">amazonmq</a><br />
<a href="/providers/aws/amplify/">amplify</a><br />
<a href="/providers/aws/amplifyuibuilder/">amplifyuibuilder</a><br />
<a href="/providers/aws/apigateway/">apigateway</a><br />
<a href="/providers/aws/apigatewayv2/">apigatewayv2</a><br />
<a href="/providers/aws/appconfig/">appconfig</a><br />
<a href="/providers/aws/appflow/">appflow</a><br />
<a href="/providers/aws/appintegrations/">appintegrations</a><br />
<a href="/providers/aws/applicationautoscaling/">applicationautoscaling</a><br />
<a href="/providers/aws/applicationinsights/">applicationinsights</a><br />
<a href="/providers/aws/appmesh/">appmesh</a><br />
<a href="/providers/aws/apprunner/">apprunner</a><br />
<a href="/providers/aws/appstream/">appstream</a><br />
<a href="/providers/aws/appsync/">appsync</a><br />
<a href="/providers/aws/aps/">aps</a><br />
<a href="/providers/aws/athena/">athena</a><br />
<a href="/providers/aws/auditmanager/">auditmanager</a><br />
<a href="/providers/aws/autoscaling/">autoscaling</a><br />
<a href="/providers/aws/autoscalingplans/">autoscalingplans</a><br />
<a href="/providers/aws/backup/">backup</a><br />
<a href="/providers/aws/batch/">batch</a><br />
<a href="/providers/aws/billingconductor/">billingconductor</a><br />
<a href="/providers/aws/budgets/">budgets</a><br />
<a href="/providers/aws/cassandra/">cassandra</a><br />
<a href="/providers/aws/ce/">ce</a><br />
<a href="/providers/aws/certificatemanager/">certificatemanager</a><br />
<a href="/providers/aws/chatbot/">chatbot</a><br />
<a href="/providers/aws/cloud9/">cloud9</a><br />
<a href="/providers/aws/cloud_control/">cloud_control</a><br />
<a href="/providers/aws/cloudformation/">cloudformation</a><br />
<a href="/providers/aws/cloudfront/">cloudfront</a><br />
<a href="/providers/aws/cloudtrail/">cloudtrail</a><br />
<a href="/providers/aws/cloudwatch/">cloudwatch</a><br />
<a href="/providers/aws/codeartifact/">codeartifact</a><br />
<a href="/providers/aws/codebuild/">codebuild</a><br />
<a href="/providers/aws/codecommit/">codecommit</a><br />
<a href="/providers/aws/codedeploy/">codedeploy</a><br />
<a href="/providers/aws/codeguruprofiler/">codeguruprofiler</a><br />
<a href="/providers/aws/codegurureviewer/">codegurureviewer</a><br />
<a href="/providers/aws/codepipeline/">codepipeline</a><br />
<a href="/providers/aws/codestar/">codestar</a><br />
<a href="/providers/aws/codestarconnections/">codestarconnections</a><br />
<a href="/providers/aws/codestarnotifications/">codestarnotifications</a><br />
<a href="/providers/aws/cognito/">cognito</a><br />
<a href="/providers/aws/comprehend/">comprehend</a><br />
<a href="/providers/aws/config/">config</a><br />
<a href="/providers/aws/connect/">connect</a><br />
<a href="/providers/aws/connectcampaigns/">connectcampaigns</a><br />
<a href="/providers/aws/controltower/">controltower</a><br />
<a href="/providers/aws/cur/">cur</a><br />
<a href="/providers/aws/customerprofiles/">customerprofiles</a><br />
<a href="/providers/aws/databrew/">databrew</a><br />
<a href="/providers/aws/datapipeline/">datapipeline</a><br />
<a href="/providers/aws/datasync/">datasync</a><br />
<a href="/providers/aws/dax/">dax</a><br />
<a href="/providers/aws/detective/">detective</a><br />
<a href="/providers/aws/devopsguru/">devopsguru</a><br />
<a href="/providers/aws/directoryservice/">directoryservice</a><br />
<a href="/providers/aws/dlm/">dlm</a><br />
<a href="/providers/aws/dms/">dms</a><br />
<a href="/providers/aws/docdb/">docdb</a><br />
<a href="/providers/aws/docdbelastic/">docdbelastic</a><br />
<a href="/providers/aws/dynamodb/">dynamodb</a><br />
<a href="/providers/aws/ec2/">ec2</a><br />
<a href="/providers/aws/ecr/">ecr</a><br />
<a href="/providers/aws/ecs/">ecs</a><br />
<a href="/providers/aws/efs/">efs</a><br />
<a href="/providers/aws/eks/">eks</a><br />
<a href="/providers/aws/elasticache/">elasticache</a><br />
<a href="/providers/aws/elasticbeanstalk/">elasticbeanstalk</a><br />
<a href="/providers/aws/elasticloadbalancing/">elasticloadbalancing</a><br />
<a href="/providers/aws/elasticloadbalancingv2/">elasticloadbalancingv2</a><br />
<a href="/providers/aws/elasticsearch/">elasticsearch</a><br />
<a href="/providers/aws/emr/">emr</a><br />
<a href="/providers/aws/emrcontainers/">emrcontainers</a><br />
<a href="/providers/aws/emrserverless/">emrserverless</a><br />
<a href="/providers/aws/events/">events</a><br />
<a href="/providers/aws/eventschemas/">eventschemas</a><br />
<a href="/providers/aws/evidently/">evidently</a><br />
<a href="/providers/aws/finspace/">finspace</a><br />
<a href="/providers/aws/fis/">fis</a><br />
<a href="/providers/aws/fms/">fms</a><br />
<a href="/providers/aws/forecast/">forecast</a><br />
<a href="/providers/aws/frauddetector/">frauddetector</a><br />
<a href="/providers/aws/fsx/">fsx</a><br />
<a href="/providers/aws/gamelift/">gamelift</a><br />
<a href="/providers/aws/globalaccelerator/">globalaccelerator</a><br />
<a href="/providers/aws/glue/">glue</a><br />
<a href="/providers/aws/grafana/">grafana</a><br />
<a href="/providers/aws/greengrass/">greengrass</a><br />
<a href="/providers/aws/greengrassv2/">greengrassv2</a><br />
<a href="/providers/aws/groundstation/">groundstation</a><br />
<a href="/providers/aws/guardduty/">guardduty</a><br />
<a href="/providers/aws/healthlake/">healthlake</a><br />
<a href="/providers/aws/iam/">iam</a><br />
<a href="/providers/aws/identitystore/">identitystore</a><br />
<a href="/providers/aws/imagebuilder/">imagebuilder</a><br />
<a href="/providers/aws/inspector/">inspector</a><br />
<a href="/providers/aws/inspectorv2/">inspectorv2</a><br />
<a href="/providers/aws/internetmonitor/">internetmonitor</a><br />
<a href="/providers/aws/iot/">iot</a><br />
<a href="/providers/aws/iot1click/">iot1click</a><br />
<a href="/providers/aws/iotanalytics/">iotanalytics</a><br />
<a href="/providers/aws/iotcoredeviceadvisor/">iotcoredeviceadvisor</a><br />
<a href="/providers/aws/iotevents/">iotevents</a><br />
</div>
<div class="providerDocColumn">
<a href="/providers/aws/iotfleethub/">iotfleethub</a><br />
<a href="/providers/aws/iotfleetwise/">iotfleetwise</a><br />
<a href="/providers/aws/iotsitewise/">iotsitewise</a><br />
<a href="/providers/aws/iotthingsgraph/">iotthingsgraph</a><br />
<a href="/providers/aws/iottwinmaker/">iottwinmaker</a><br />
<a href="/providers/aws/iotwireless/">iotwireless</a><br />
<a href="/providers/aws/ivs/">ivs</a><br />
<a href="/providers/aws/ivschat/">ivschat</a><br />
<a href="/providers/aws/kafkaconnect/">kafkaconnect</a><br />
<a href="/providers/aws/kendra/">kendra</a><br />
<a href="/providers/aws/kendraranking/">kendraranking</a><br />
<a href="/providers/aws/kinesis/">kinesis</a><br />
<a href="/providers/aws/kinesisanalytics/">kinesisanalytics</a><br />
<a href="/providers/aws/kinesisanalyticsv2/">kinesisanalyticsv2</a><br />
<a href="/providers/aws/kinesisfirehose/">kinesisfirehose</a><br />
<a href="/providers/aws/kinesisvideo/">kinesisvideo</a><br />
<a href="/providers/aws/kms/">kms</a><br />
<a href="/providers/aws/lakeformation/">lakeformation</a><br />
<a href="/providers/aws/lambda/">lambda</a><br />
<a href="/providers/aws/lex/">lex</a><br />
<a href="/providers/aws/licensemanager/">licensemanager</a><br />
<a href="/providers/aws/lightsail/">lightsail</a><br />
<a href="/providers/aws/location/">location</a><br />
<a href="/providers/aws/logs/">logs</a><br />
<a href="/providers/aws/lookoutequipment/">lookoutequipment</a><br />
<a href="/providers/aws/lookoutmetrics/">lookoutmetrics</a><br />
<a href="/providers/aws/lookoutvision/">lookoutvision</a><br />
<a href="/providers/aws/m2/">m2</a><br />
<a href="/providers/aws/macie/">macie</a><br />
<a href="/providers/aws/managedblockchain/">managedblockchain</a><br />
<a href="/providers/aws/mediaconnect/">mediaconnect</a><br />
<a href="/providers/aws/mediaconvert/">mediaconvert</a><br />
<a href="/providers/aws/medialive/">medialive</a><br />
<a href="/providers/aws/mediapackage/">mediapackage</a><br />
<a href="/providers/aws/mediastore/">mediastore</a><br />
<a href="/providers/aws/mediatailor/">mediatailor</a><br />
<a href="/providers/aws/memorydb/">memorydb</a><br />
<a href="/providers/aws/msk/">msk</a><br />
<a href="/providers/aws/mwaa/">mwaa</a><br />
<a href="/providers/aws/neptune/">neptune</a><br />
<a href="/providers/aws/networkfirewall/">networkfirewall</a><br />
<a href="/providers/aws/networkmanager/">networkmanager</a><br />
<a href="/providers/aws/nimblestudio/">nimblestudio</a><br />
<a href="/providers/aws/oam/">oam</a><br />
<a href="/providers/aws/omics/">omics</a><br />
<a href="/providers/aws/opensearchserverless/">opensearchserverless</a><br />
<a href="/providers/aws/opensearchservice/">opensearchservice</a><br />
<a href="/providers/aws/opsworks/">opsworks</a><br />
<a href="/providers/aws/opsworkscm/">opsworkscm</a><br />
<a href="/providers/aws/organizations/">organizations</a><br />
<a href="/providers/aws/panorama/">panorama</a><br />
<a href="/providers/aws/personalize/">personalize</a><br />
<a href="/providers/aws/pinpoint/">pinpoint</a><br />
<a href="/providers/aws/pinpointemail/">pinpointemail</a><br />
<a href="/providers/aws/pipes/">pipes</a><br />
<a href="/providers/aws/qldb/">qldb</a><br />
<a href="/providers/aws/quicksight/">quicksight</a><br />
<a href="/providers/aws/ram/">ram</a><br />
<a href="/providers/aws/rds/">rds</a><br />
<a href="/providers/aws/redshift/">redshift</a><br />
<a href="/providers/aws/redshiftserverless/">redshiftserverless</a><br />
<a href="/providers/aws/refactorspaces/">refactorspaces</a><br />
<a href="/providers/aws/rekognition/">rekognition</a><br />
<a href="/providers/aws/resiliencehub/">resiliencehub</a><br />
<a href="/providers/aws/resourceexplorer2/">resourceexplorer2</a><br />
<a href="/providers/aws/resourcegroups/">resourcegroups</a><br />
<a href="/providers/aws/robomaker/">robomaker</a><br />
<a href="/providers/aws/rolesanywhere/">rolesanywhere</a><br />
<a href="/providers/aws/route53/">route53</a><br />
<a href="/providers/aws/route53recoverycontrol/">route53recoverycontrol</a><br />
<a href="/providers/aws/route53recoveryreadiness/">route53recoveryreadiness</a><br />
<a href="/providers/aws/route53resolver/">route53resolver</a><br />
<a href="/providers/aws/rum/">rum</a><br />
<a href="/providers/aws/s3/">s3</a><br />
<a href="/providers/aws/s3objectlambda/">s3objectlambda</a><br />
<a href="/providers/aws/s3outposts/">s3outposts</a><br />
<a href="/providers/aws/sagemaker/">sagemaker</a><br />
<a href="/providers/aws/scheduler/">scheduler</a><br />
<a href="/providers/aws/sdb/">sdb</a><br />
<a href="/providers/aws/secretsmanager/">secretsmanager</a><br />
<a href="/providers/aws/securityhub/">securityhub</a><br />
<a href="/providers/aws/servicecatalog/">servicecatalog</a><br />
<a href="/providers/aws/servicecatalogappregistry/">servicecatalogappregistry</a><br />
<a href="/providers/aws/servicediscovery/">servicediscovery</a><br />
<a href="/providers/aws/ses/">ses</a><br />
<a href="/providers/aws/signer/">signer</a><br />
<a href="/providers/aws/simspaceweaver/">simspaceweaver</a><br />
<a href="/providers/aws/sns/">sns</a><br />
<a href="/providers/aws/sqs/">sqs</a><br />
<a href="/providers/aws/ssm/">ssm</a><br />
<a href="/providers/aws/ssmcontacts/">ssmcontacts</a><br />
<a href="/providers/aws/ssmincidents/">ssmincidents</a><br />
<a href="/providers/aws/sso/">sso</a><br />
<a href="/providers/aws/stepfunctions/">stepfunctions</a><br />
<a href="/providers/aws/supportapp/">supportapp</a><br />
<a href="/providers/aws/synthetics/">synthetics</a><br />
<a href="/providers/aws/systemsmanagersap/">systemsmanagersap</a><br />
<a href="/providers/aws/timestream/">timestream</a><br />
<a href="/providers/aws/transfer/">transfer</a><br />
<a href="/providers/aws/voiceid/">voiceid</a><br />
<a href="/providers/aws/vpclattice/">vpclattice</a><br />
<a href="/providers/aws/waf/">waf</a><br />
<a href="/providers/aws/wafregional/">wafregional</a><br />
<a href="/providers/aws/wafv2/">wafv2</a><br />
<a href="/providers/aws/wisdom/">wisdom</a><br />
<a href="/providers/aws/workspaces/">workspaces</a><br />
<a href="/providers/aws/xray/">xray</a><br />
</div>
</div>
