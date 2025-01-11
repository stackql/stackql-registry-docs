---
title: connector_profiles
hide_title: false
hide_table_of_contents: false
keywords:
  - connector_profiles
  - appflow
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes or gets a <code>connector_profile</code> resource or lists <code>connector_profiles</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>connector_profiles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::AppFlow::ConnectorProfile</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.appflow.connector_profiles" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="connector_profile_arn" /></td><td><code>string</code></td><td>Unique identifier for connector profile resources</td></tr>
<tr><td><CopyableCode code="connector_label" /></td><td><code>string</code></td><td>The label of the connector. The label is unique for each ConnectorRegistration in your AWS account. Only needed if calling for CUSTOMCONNECTOR connector type/.</td></tr>
<tr><td><CopyableCode code="connector_profile_name" /></td><td><code>string</code></td><td>The maximum number of items to retrieve in a single batch.</td></tr>
<tr><td><CopyableCode code="kms_arn" /></td><td><code>string</code></td><td>The ARN of the AWS Key Management Service (AWS KMS) key that's used to encrypt your function's environment variables. If it's not provided, AWS Lambda uses a default service key.</td></tr>
<tr><td><CopyableCode code="connector_type" /></td><td><code>string</code></td><td>List of Saas providers that need connector profile to be created</td></tr>
<tr><td><CopyableCode code="connection_mode" /></td><td><code>string</code></td><td>Mode in which data transfer should be enabled. Private connection mode is currently enabled for Salesforce, Snowflake, Trendmicro and Singular</td></tr>
<tr><td><CopyableCode code="connector_profile_config" /></td><td><code>object</code></td><td>Connector specific configurations needed to create connector profile</td></tr>
<tr><td><CopyableCode code="credentials_arn" /></td><td><code>string</code></td><td>A unique Arn for Connector-Profile resource</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appflow-connectorprofile.html"><code>AWS::AppFlow::ConnectorProfile</code></a>.

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="ConnectorProfileName, ConnectionMode, ConnectorType, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Gets all <code>connector_profiles</code> in a region.
```sql
SELECT
region,
connector_profile_arn,
connector_label,
connector_profile_name,
kms_arn,
connector_type,
connection_mode,
connector_profile_config,
credentials_arn
FROM aws.appflow.connector_profiles
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>connector_profile</code>.
```sql
SELECT
region,
connector_profile_arn,
connector_label,
connector_profile_name,
kms_arn,
connector_type,
connection_mode,
connector_profile_config,
credentials_arn
FROM aws.appflow.connector_profiles
WHERE region = 'us-east-1' AND data__Identifier = '<ConnectorProfileName>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>connector_profile</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
      { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="required">

```sql
/*+ create */
INSERT INTO aws.appflow.connector_profiles (
 ConnectorProfileName,
 ConnectorType,
 ConnectionMode,
 region
)
SELECT 
'{{ ConnectorProfileName }}',
 '{{ ConnectorType }}',
 '{{ ConnectionMode }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.appflow.connector_profiles (
 ConnectorLabel,
 ConnectorProfileName,
 KMSArn,
 ConnectorType,
 ConnectionMode,
 ConnectorProfileConfig,
 region
)
SELECT 
 '{{ ConnectorLabel }}',
 '{{ ConnectorProfileName }}',
 '{{ KMSArn }}',
 '{{ ConnectorType }}',
 '{{ ConnectionMode }}',
 '{{ ConnectorProfileConfig }}',
 '{{ region }}';
```
</TabItem>
<TabItem value="manifest">

```yaml
version: 1
name: stack name
description: stack description
providers:
  - aws
globals:
  - name: region
    value: '{{ vars.AWS_REGION }}'
resources:
  - name: connector_profile
    props:
      - name: ConnectorLabel
        value: '{{ ConnectorLabel }}'
      - name: ConnectorProfileName
        value: '{{ ConnectorProfileName }}'
      - name: KMSArn
        value: '{{ KMSArn }}'
      - name: ConnectorType
        value: '{{ ConnectorType }}'
      - name: ConnectionMode
        value: '{{ ConnectionMode }}'
      - name: ConnectorProfileConfig
        value:
          ConnectorProfileProperties:
            Datadog:
              InstanceUrl: '{{ InstanceUrl }}'
            Dynatrace:
              InstanceUrl: null
            InforNexus:
              InstanceUrl: null
            Marketo:
              InstanceUrl: null
            Redshift:
              DatabaseUrl: '{{ DatabaseUrl }}'
              BucketName: '{{ BucketName }}'
              BucketPrefix: '{{ BucketPrefix }}'
              RoleArn: '{{ RoleArn }}'
              IsRedshiftServerless: '{{ IsRedshiftServerless }}'
              DataApiRoleArn: '{{ DataApiRoleArn }}'
              ClusterIdentifier: '{{ ClusterIdentifier }}'
              WorkgroupName: '{{ WorkgroupName }}'
              DatabaseName: '{{ DatabaseName }}'
            SAPOData:
              ApplicationHostUrl: '{{ ApplicationHostUrl }}'
              ApplicationServicePath: '{{ ApplicationServicePath }}'
              PortNumber: '{{ PortNumber }}'
              ClientNumber: '{{ ClientNumber }}'
              LogonLanguage: '{{ LogonLanguage }}'
              PrivateLinkServiceName: '{{ PrivateLinkServiceName }}'
              OAuthProperties:
                AuthCodeUrl: '{{ AuthCodeUrl }}'
                TokenUrl: '{{ TokenUrl }}'
                OAuthScopes:
                  - '{{ OAuthScopes[0] }}'
              DisableSSO: '{{ DisableSSO }}'
            Salesforce:
              InstanceUrl: null
              isSandboxEnvironment: '{{ isSandboxEnvironment }}'
              usePrivateLinkForMetadataAndAuthorization: '{{ usePrivateLinkForMetadataAndAuthorization }}'
            Pardot:
              InstanceUrl: null
              IsSandboxEnvironment: '{{ IsSandboxEnvironment }}'
              BusinessUnitId: '{{ BusinessUnitId }}'
            ServiceNow:
              InstanceUrl: null
            Slack:
              InstanceUrl: null
            Snowflake:
              Warehouse: '{{ Warehouse }}'
              Stage: '{{ Stage }}'
              BucketName: null
              BucketPrefix: null
              PrivateLinkServiceName: null
              AccountName: '{{ AccountName }}'
              Region: '{{ Region }}'
            Veeva:
              InstanceUrl: null
            Zendesk:
              InstanceUrl: null
            CustomConnector:
              ProfileProperties: {}
              OAuth2Properties:
                TokenUrl: '{{ TokenUrl }}'
                OAuth2GrantType: '{{ OAuth2GrantType }}'
                TokenUrlCustomProperties: {}
          ConnectorProfileCredentials:
            Amplitude:
              ApiKey: '{{ ApiKey }}'
              SecretKey: '{{ SecretKey }}'
            Datadog:
              ApiKey: null
              ApplicationKey: '{{ ApplicationKey }}'
            Dynatrace:
              ApiToken: '{{ ApiToken }}'
            GoogleAnalytics:
              ClientId: '{{ ClientId }}'
              ClientSecret: '{{ ClientSecret }}'
              AccessToken: '{{ AccessToken }}'
              RefreshToken: '{{ RefreshToken }}'
              ConnectorOAuthRequest:
                AuthCode: '{{ AuthCode }}'
                RedirectUri: '{{ RedirectUri }}'
            InforNexus:
              AccessKeyId: '{{ AccessKeyId }}'
              UserId: '{{ UserId }}'
              SecretAccessKey: '{{ SecretAccessKey }}'
              Datakey: null
            Marketo:
              ClientId: null
              ClientSecret: null
              AccessToken: null
              ConnectorOAuthRequest: null
            Redshift:
              Username: null
              Password: '{{ Password }}'
            SAPOData:
              BasicAuthCredentials:
                Username: null
                Password: null
              OAuthCredentials:
                AccessToken: null
                RefreshToken: null
                ConnectorOAuthRequest: null
                ClientId: null
                ClientSecret: null
            Salesforce:
              AccessToken: null
              RefreshToken: null
              ConnectorOAuthRequest: null
              ClientCredentialsArn: '{{ ClientCredentialsArn }}'
              OAuth2GrantType: null
              JwtToken: '{{ JwtToken }}'
            Pardot:
              AccessToken: null
              RefreshToken: null
              ConnectorOAuthRequest: null
              ClientCredentialsArn: null
            ServiceNow:
              Username: null
              Password: null
              OAuth2Credentials:
                ClientId: null
                ClientSecret: null
                AccessToken: null
                RefreshToken: null
                OAuthRequest: null
            Singular:
              ApiKey: null
            Slack:
              ClientId: null
              ClientSecret: null
              AccessToken: null
              ConnectorOAuthRequest: null
            Snowflake:
              Username: null
              Password: null
            Trendmicro:
              ApiSecretKey: '{{ ApiSecretKey }}'
            Veeva:
              Username: null
              Password: null
            Zendesk:
              ClientId: null
              ClientSecret: null
              AccessToken: null
              ConnectorOAuthRequest: null
            CustomConnector:
              AuthenticationType: '{{ AuthenticationType }}'
              Basic: null
              Oauth2: null
              ApiKey:
                ApiKey: null
                ApiSecretKey: null
              Custom:
                CustomAuthenticationType: '{{ CustomAuthenticationType }}'
                CredentialsMap: {}

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.appflow.connector_profiles
WHERE data__Identifier = '<ConnectorProfileName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>connector_profiles</code> resource, the following permissions are required:

### Create
```json
appflow:CreateConnectorProfile,
kms:ListKeys,
kms:DescribeKey,
kms:ListAliases,
kms:CreateGrant,
kms:ListGrants,
iam:PassRole,
secretsmanager:CreateSecret,
secretsmanager:GetSecretValue,
secretsmanager:PutResourcePolicy
```

### Delete
```json
appflow:DeleteConnectorProfile
```

### List
```json
appflow:DescribeConnectorProfiles
```

### Read
```json
appflow:DescribeConnectorProfiles
```

### Update
```json
appflow:UpdateConnectorProfile,
kms:ListKeys,
kms:DescribeKey,
kms:ListAliases,
kms:CreateGrant,
kms:ListGrants,
iam:PassRole,
secretsmanager:CreateSecret,
secretsmanager:GetSecretValue,
secretsmanager:PutResourcePolicy
```
