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


Used to retrieve a list of <code>connector_profiles</code> in a region or to create or delete a <code>connector_profiles</code> resource, use <code>connector_profile</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>connector_profiles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::AppFlow::ConnectorProfile</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.appflow.connector_profiles" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="connector_profile_name" /></td><td><code>string</code></td><td>The maximum number of items to retrieve in a single batch.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

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
    <td><CopyableCode code="data__DesiredState, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
connector_profile_name
FROM aws.appflow.connector_profiles
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>connector_profile</code> resource, using <a ref="https://pypi.org/project/stack-deploy/" target="_blank"><code><b>stack-deploy</b></code></a>.

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
-- connector_profile.iql (required properties only)
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
-- connector_profile.iql (all properties)
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

## `DELETE` Example

```sql
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

