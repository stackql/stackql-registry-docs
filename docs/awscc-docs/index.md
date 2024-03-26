---
title: awscc
hide_title: false
hide_table_of_contents: false
keywords:
  - aws
  - aws cloud control
  - cloud control api
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
id: awscc-doc
slug: /providers/awscc

---
Cloud services from AWS using the Cloud Control API.

:::info Provider Summary (v24.03.00220)

<div class="row">
<div class="providerDocColumn">
<span>total services:&nbsp;<b>208</b></span><br />
<span>total methods:&nbsp;<b>1,792</b></span><br />
</div>
<div class="providerDocColumn">
<span>total resources:&nbsp;<b>1,788</b></span><br />
<span>total selectable resources:&nbsp;<b>1,788</b></span><br />
</div>
</div>

:::

See also:   
[[` SHOW `]](https://stackql.io/docs/language-spec/show) [[` DESCRIBE `]](https://stackql.io/docs/language-spec/describe)  [[` REGISTRY `]](https://stackql.io/docs/language-spec/registry)
* * * 

## Installation

To pull the latest version of the `awscc` provider, run the following command:  

```bash
REGISTRY PULL awscc;
```
> To view previous provider versions or to pull a specific provider version, see [here](https://stackql.io/docs/language-spec/registry).  

## Authentication

The following system environment variables are used for authentication by default:  

- `AWS_ACCESS_KEY_ID` - AWS Access Key ID (see [How to Create AWS Credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html))
- `AWS_SECRET_ACCESS_KEY` - AWS Secret Access Key (see [How to Create AWS Credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html))
- `AWS_SESSION_TOKEN` - [*OPTIONAL:* only required if using `aws sts assume-role`] AWS Session Token (see [Temporary security credentials in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html))
  
These variables are sourced at runtime (from the local machine or as CI variables/secrets).  

<details>

<summary>Using different environment variables</summary>

To use different environment variables (instead of the defaults), use the `--auth` flag of the `stackql` program.  For example:  

```bash

AUTH='{ "awscc": { "type": "aws_signing_v4", "keyIDenvvar": "YOUR_ACCESS_KEY_ID_VAR", "credentialsenvvar": "YOUR_SECRET_KEY_VAR" }}'
stackql shell --auth="${AUTH}"

```
or using PowerShell:  

```powershell

$Auth = "{ 'awscc': { 'type': 'aws_signing_v4',  'keyIDenvvar': 'YOUR_ACCESS_KEY_ID_VAR', 'credentialsenvvar': 'YOUR_SECRET_KEY_VAR' }}"
stackql.exe shell --auth=$Auth

```
</details>


## Server Parameters


The following parameter is required for the `awscc` provider:  

- `region` - AWS region (e.g. `us-east-1`)

This parameter must be supplied to the `WHERE` clause of each `SELECT` statement.

## Services
<div class="row">
<div class="providerDocColumn">
<a href="/providers/awscc/accessanalyzer/">accessanalyzer</a><br />
<a href="/providers/awscc/acmpca/">acmpca</a><br />
<a href="/providers/awscc/amplify/">amplify</a><br />
<a href="/providers/awscc/amplifyuibuilder/">amplifyuibuilder</a><br />
<a href="/providers/awscc/apigateway/">apigateway</a><br />
<a href="/providers/awscc/apigatewayv2/">apigatewayv2</a><br />
<a href="/providers/awscc/appconfig/">appconfig</a><br />
<a href="/providers/awscc/appflow/">appflow</a><br />
<a href="/providers/awscc/appintegrations/">appintegrations</a><br />
<a href="/providers/awscc/applicationautoscaling/">applicationautoscaling</a><br />
<a href="/providers/awscc/applicationinsights/">applicationinsights</a><br />
<a href="/providers/awscc/apprunner/">apprunner</a><br />
<a href="/providers/awscc/appstream/">appstream</a><br />
<a href="/providers/awscc/appsync/">appsync</a><br />
<a href="/providers/awscc/aps/">aps</a><br />
<a href="/providers/awscc/arczonalshift/">arczonalshift</a><br />
<a href="/providers/awscc/athena/">athena</a><br />
<a href="/providers/awscc/auditmanager/">auditmanager</a><br />
<a href="/providers/awscc/autoscaling/">autoscaling</a><br />
<a href="/providers/awscc/b2bi/">b2bi</a><br />
<a href="/providers/awscc/backup/">backup</a><br />
<a href="/providers/awscc/backupgateway/">backupgateway</a><br />
<a href="/providers/awscc/batch/">batch</a><br />
<a href="/providers/awscc/billingconductor/">billingconductor</a><br />
<a href="/providers/awscc/budgets/">budgets</a><br />
<a href="/providers/awscc/cassandra/">cassandra</a><br />
<a href="/providers/awscc/ce/">ce</a><br />
<a href="/providers/awscc/certificatemanager/">certificatemanager</a><br />
<a href="/providers/awscc/chatbot/">chatbot</a><br />
<a href="/providers/awscc/cleanrooms/">cleanrooms</a><br />
<a href="/providers/awscc/cloud_control/">cloud_control</a><br />
<a href="/providers/awscc/cloudformation/">cloudformation</a><br />
<a href="/providers/awscc/cloudfront/">cloudfront</a><br />
<a href="/providers/awscc/cloudtrail/">cloudtrail</a><br />
<a href="/providers/awscc/cloudwatch/">cloudwatch</a><br />
<a href="/providers/awscc/codeartifact/">codeartifact</a><br />
<a href="/providers/awscc/codebuild/">codebuild</a><br />
<a href="/providers/awscc/codedeploy/">codedeploy</a><br />
<a href="/providers/awscc/codeguruprofiler/">codeguruprofiler</a><br />
<a href="/providers/awscc/codegurureviewer/">codegurureviewer</a><br />
<a href="/providers/awscc/codepipeline/">codepipeline</a><br />
<a href="/providers/awscc/codestarconnections/">codestarconnections</a><br />
<a href="/providers/awscc/codestarnotifications/">codestarnotifications</a><br />
<a href="/providers/awscc/cognito/">cognito</a><br />
<a href="/providers/awscc/comprehend/">comprehend</a><br />
<a href="/providers/awscc/config/">config</a><br />
<a href="/providers/awscc/connect/">connect</a><br />
<a href="/providers/awscc/connectcampaigns/">connectcampaigns</a><br />
<a href="/providers/awscc/controltower/">controltower</a><br />
<a href="/providers/awscc/cur/">cur</a><br />
<a href="/providers/awscc/customerprofiles/">customerprofiles</a><br />
<a href="/providers/awscc/databrew/">databrew</a><br />
<a href="/providers/awscc/datapipeline/">datapipeline</a><br />
<a href="/providers/awscc/datasync/">datasync</a><br />
<a href="/providers/awscc/datazone/">datazone</a><br />
<a href="/providers/awscc/detective/">detective</a><br />
<a href="/providers/awscc/devopsguru/">devopsguru</a><br />
<a href="/providers/awscc/directoryservice/">directoryservice</a><br />
<a href="/providers/awscc/dms/">dms</a><br />
<a href="/providers/awscc/docdbelastic/">docdbelastic</a><br />
<a href="/providers/awscc/dynamodb/">dynamodb</a><br />
<a href="/providers/awscc/ec2/">ec2</a><br />
<a href="/providers/awscc/ecr/">ecr</a><br />
<a href="/providers/awscc/ecs/">ecs</a><br />
<a href="/providers/awscc/efs/">efs</a><br />
<a href="/providers/awscc/eks/">eks</a><br />
<a href="/providers/awscc/elasticache/">elasticache</a><br />
<a href="/providers/awscc/elasticbeanstalk/">elasticbeanstalk</a><br />
<a href="/providers/awscc/elasticloadbalancingv2/">elasticloadbalancingv2</a><br />
<a href="/providers/awscc/emr/">emr</a><br />
<a href="/providers/awscc/emrcontainers/">emrcontainers</a><br />
<a href="/providers/awscc/emrserverless/">emrserverless</a><br />
<a href="/providers/awscc/entityresolution/">entityresolution</a><br />
<a href="/providers/awscc/events/">events</a><br />
<a href="/providers/awscc/eventschemas/">eventschemas</a><br />
<a href="/providers/awscc/evidently/">evidently</a><br />
<a href="/providers/awscc/finspace/">finspace</a><br />
<a href="/providers/awscc/fis/">fis</a><br />
<a href="/providers/awscc/fms/">fms</a><br />
<a href="/providers/awscc/forecast/">forecast</a><br />
<a href="/providers/awscc/frauddetector/">frauddetector</a><br />
<a href="/providers/awscc/fsx/">fsx</a><br />
<a href="/providers/awscc/gamelift/">gamelift</a><br />
<a href="/providers/awscc/globalaccelerator/">globalaccelerator</a><br />
<a href="/providers/awscc/glue/">glue</a><br />
<a href="/providers/awscc/grafana/">grafana</a><br />
<a href="/providers/awscc/greengrassv2/">greengrassv2</a><br />
<a href="/providers/awscc/groundstation/">groundstation</a><br />
<a href="/providers/awscc/guardduty/">guardduty</a><br />
<a href="/providers/awscc/healthimaging/">healthimaging</a><br />
<a href="/providers/awscc/healthlake/">healthlake</a><br />
<a href="/providers/awscc/iam/">iam</a><br />
<a href="/providers/awscc/identitystore/">identitystore</a><br />
<a href="/providers/awscc/imagebuilder/">imagebuilder</a><br />
<a href="/providers/awscc/inspector/">inspector</a><br />
<a href="/providers/awscc/inspectorv2/">inspectorv2</a><br />
<a href="/providers/awscc/internetmonitor/">internetmonitor</a><br />
<a href="/providers/awscc/iot/">iot</a><br />
<a href="/providers/awscc/iotanalytics/">iotanalytics</a><br />
<a href="/providers/awscc/iotcoredeviceadvisor/">iotcoredeviceadvisor</a><br />
<a href="/providers/awscc/iotevents/">iotevents</a><br />
<a href="/providers/awscc/iotfleethub/">iotfleethub</a><br />
<a href="/providers/awscc/iotfleetwise/">iotfleetwise</a><br />
<a href="/providers/awscc/iotsitewise/">iotsitewise</a><br />
</div>
<div class="providerDocColumn">
<a href="/providers/awscc/iottwinmaker/">iottwinmaker</a><br />
<a href="/providers/awscc/iotwireless/">iotwireless</a><br />
<a href="/providers/awscc/ivs/">ivs</a><br />
<a href="/providers/awscc/ivschat/">ivschat</a><br />
<a href="/providers/awscc/kafkaconnect/">kafkaconnect</a><br />
<a href="/providers/awscc/kendra/">kendra</a><br />
<a href="/providers/awscc/kendraranking/">kendraranking</a><br />
<a href="/providers/awscc/kinesis/">kinesis</a><br />
<a href="/providers/awscc/kinesisanalyticsv2/">kinesisanalyticsv2</a><br />
<a href="/providers/awscc/kinesisfirehose/">kinesisfirehose</a><br />
<a href="/providers/awscc/kinesisvideo/">kinesisvideo</a><br />
<a href="/providers/awscc/kms/">kms</a><br />
<a href="/providers/awscc/lakeformation/">lakeformation</a><br />
<a href="/providers/awscc/lambda/">lambda</a><br />
<a href="/providers/awscc/lex/">lex</a><br />
<a href="/providers/awscc/licensemanager/">licensemanager</a><br />
<a href="/providers/awscc/lightsail/">lightsail</a><br />
<a href="/providers/awscc/location/">location</a><br />
<a href="/providers/awscc/logs/">logs</a><br />
<a href="/providers/awscc/lookoutequipment/">lookoutequipment</a><br />
<a href="/providers/awscc/lookoutmetrics/">lookoutmetrics</a><br />
<a href="/providers/awscc/lookoutvision/">lookoutvision</a><br />
<a href="/providers/awscc/m2/">m2</a><br />
<a href="/providers/awscc/macie/">macie</a><br />
<a href="/providers/awscc/managedblockchain/">managedblockchain</a><br />
<a href="/providers/awscc/mediaconnect/">mediaconnect</a><br />
<a href="/providers/awscc/medialive/">medialive</a><br />
<a href="/providers/awscc/mediapackage/">mediapackage</a><br />
<a href="/providers/awscc/mediapackagev2/">mediapackagev2</a><br />
<a href="/providers/awscc/mediatailor/">mediatailor</a><br />
<a href="/providers/awscc/memorydb/">memorydb</a><br />
<a href="/providers/awscc/msk/">msk</a><br />
<a href="/providers/awscc/mwaa/">mwaa</a><br />
<a href="/providers/awscc/neptune/">neptune</a><br />
<a href="/providers/awscc/neptunegraph/">neptunegraph</a><br />
<a href="/providers/awscc/networkfirewall/">networkfirewall</a><br />
<a href="/providers/awscc/networkmanager/">networkmanager</a><br />
<a href="/providers/awscc/nimblestudio/">nimblestudio</a><br />
<a href="/providers/awscc/oam/">oam</a><br />
<a href="/providers/awscc/omics/">omics</a><br />
<a href="/providers/awscc/opensearchserverless/">opensearchserverless</a><br />
<a href="/providers/awscc/opensearchservice/">opensearchservice</a><br />
<a href="/providers/awscc/opsworkscm/">opsworkscm</a><br />
<a href="/providers/awscc/organizations/">organizations</a><br />
<a href="/providers/awscc/osis/">osis</a><br />
<a href="/providers/awscc/panorama/">panorama</a><br />
<a href="/providers/awscc/pcaconnectorad/">pcaconnectorad</a><br />
<a href="/providers/awscc/personalize/">personalize</a><br />
<a href="/providers/awscc/pinpoint/">pinpoint</a><br />
<a href="/providers/awscc/pipes/">pipes</a><br />
<a href="/providers/awscc/proton/">proton</a><br />
<a href="/providers/awscc/qldb/">qldb</a><br />
<a href="/providers/awscc/quicksight/">quicksight</a><br />
<a href="/providers/awscc/ram/">ram</a><br />
<a href="/providers/awscc/rds/">rds</a><br />
<a href="/providers/awscc/redshift/">redshift</a><br />
<a href="/providers/awscc/redshiftserverless/">redshiftserverless</a><br />
<a href="/providers/awscc/refactorspaces/">refactorspaces</a><br />
<a href="/providers/awscc/rekognition/">rekognition</a><br />
<a href="/providers/awscc/resiliencehub/">resiliencehub</a><br />
<a href="/providers/awscc/resourceexplorer2/">resourceexplorer2</a><br />
<a href="/providers/awscc/resourcegroups/">resourcegroups</a><br />
<a href="/providers/awscc/robomaker/">robomaker</a><br />
<a href="/providers/awscc/rolesanywhere/">rolesanywhere</a><br />
<a href="/providers/awscc/route53/">route53</a><br />
<a href="/providers/awscc/route53recoverycontrol/">route53recoverycontrol</a><br />
<a href="/providers/awscc/route53recoveryreadiness/">route53recoveryreadiness</a><br />
<a href="/providers/awscc/route53resolver/">route53resolver</a><br />
<a href="/providers/awscc/rum/">rum</a><br />
<a href="/providers/awscc/s3/">s3</a><br />
<a href="/providers/awscc/s3express/">s3express</a><br />
<a href="/providers/awscc/s3objectlambda/">s3objectlambda</a><br />
<a href="/providers/awscc/s3outposts/">s3outposts</a><br />
<a href="/providers/awscc/sagemaker/">sagemaker</a><br />
<a href="/providers/awscc/scheduler/">scheduler</a><br />
<a href="/providers/awscc/secretsmanager/">secretsmanager</a><br />
<a href="/providers/awscc/securityhub/">securityhub</a><br />
<a href="/providers/awscc/servicecatalog/">servicecatalog</a><br />
<a href="/providers/awscc/servicecatalogappregistry/">servicecatalogappregistry</a><br />
<a href="/providers/awscc/ses/">ses</a><br />
<a href="/providers/awscc/shield/">shield</a><br />
<a href="/providers/awscc/signer/">signer</a><br />
<a href="/providers/awscc/simspaceweaver/">simspaceweaver</a><br />
<a href="/providers/awscc/sns/">sns</a><br />
<a href="/providers/awscc/sqs/">sqs</a><br />
<a href="/providers/awscc/ssm/">ssm</a><br />
<a href="/providers/awscc/ssmcontacts/">ssmcontacts</a><br />
<a href="/providers/awscc/ssmincidents/">ssmincidents</a><br />
<a href="/providers/awscc/sso/">sso</a><br />
<a href="/providers/awscc/stepfunctions/">stepfunctions</a><br />
<a href="/providers/awscc/supportapp/">supportapp</a><br />
<a href="/providers/awscc/synthetics/">synthetics</a><br />
<a href="/providers/awscc/systemsmanagersap/">systemsmanagersap</a><br />
<a href="/providers/awscc/timestream/">timestream</a><br />
<a href="/providers/awscc/transfer/">transfer</a><br />
<a href="/providers/awscc/verifiedpermissions/">verifiedpermissions</a><br />
<a href="/providers/awscc/voiceid/">voiceid</a><br />
<a href="/providers/awscc/vpclattice/">vpclattice</a><br />
<a href="/providers/awscc/wafv2/">wafv2</a><br />
<a href="/providers/awscc/wisdom/">wisdom</a><br />
<a href="/providers/awscc/workspaces/">workspaces</a><br />
<a href="/providers/awscc/workspacesthinclient/">workspacesthinclient</a><br />
<a href="/providers/awscc/workspacesweb/">workspacesweb</a><br />
<a href="/providers/awscc/xray/">xray</a><br />
</div>
</div>
