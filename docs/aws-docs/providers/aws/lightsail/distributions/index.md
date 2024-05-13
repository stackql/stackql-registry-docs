---
title: distributions
hide_title: false
hide_table_of_contents: false
keywords:
  - distributions
  - lightsail
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


Used to retrieve a list of <code>distributions</code> in a region or to create or delete a <code>distributions</code> resource, use <code>distribution</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>distributions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Lightsail::Distribution</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.lightsail.distributions" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="distribution_name" /></td><td><code>string</code></td><td>The name for the distribution.</td></tr>
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
    <td><CopyableCode code="DistributionName, BundleId, DefaultCacheBehavior, Origin, region" /></td>
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
distribution_name
FROM aws.lightsail.distributions
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>distribution</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.lightsail.distributions (
 DistributionName,
 BundleId,
 DefaultCacheBehavior,
 Origin,
 region
)
SELECT 
'{{ DistributionName }}',
 '{{ BundleId }}',
 '{{ DefaultCacheBehavior }}',
 '{{ Origin }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.lightsail.distributions (
 DistributionName,
 BundleId,
 IpAddressType,
 CacheBehaviors,
 CacheBehaviorSettings,
 DefaultCacheBehavior,
 Origin,
 IsEnabled,
 CertificateName,
 Tags,
 region
)
SELECT 
 '{{ DistributionName }}',
 '{{ BundleId }}',
 '{{ IpAddressType }}',
 '{{ CacheBehaviors }}',
 '{{ CacheBehaviorSettings }}',
 '{{ DefaultCacheBehavior }}',
 '{{ Origin }}',
 '{{ IsEnabled }}',
 '{{ CertificateName }}',
 '{{ Tags }}',
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
  - name: distribution
    props:
      - name: DistributionName
        value: '{{ DistributionName }}'
      - name: BundleId
        value: '{{ BundleId }}'
      - name: IpAddressType
        value: '{{ IpAddressType }}'
      - name: CacheBehaviors
        value:
          - Behavior: '{{ Behavior }}'
            Path: '{{ Path }}'
      - name: CacheBehaviorSettings
        value:
          AllowedHTTPMethods: '{{ AllowedHTTPMethods }}'
          CachedHTTPMethods: '{{ CachedHTTPMethods }}'
          DefaultTTL: '{{ DefaultTTL }}'
          MaximumTTL: '{{ MaximumTTL }}'
          MinimumTTL: '{{ MinimumTTL }}'
          ForwardedCookies:
            CookiesAllowList:
              - '{{ CookiesAllowList[0] }}'
            Option: '{{ Option }}'
          ForwardedHeaders:
            HeadersAllowList:
              - '{{ HeadersAllowList[0] }}'
            Option: '{{ Option }}'
          ForwardedQueryStrings:
            QueryStringsAllowList:
              - '{{ QueryStringsAllowList[0] }}'
            Option: '{{ Option }}'
      - name: DefaultCacheBehavior
        value:
          Behavior: '{{ Behavior }}'
      - name: Origin
        value:
          Name: '{{ Name }}'
          ProtocolPolicy: '{{ ProtocolPolicy }}'
          RegionName: '{{ RegionName }}'
      - name: IsEnabled
        value: '{{ IsEnabled }}'
      - name: CertificateName
        value: '{{ CertificateName }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
/*+ delete */
DELETE FROM aws.lightsail.distributions
WHERE data__Identifier = '<DistributionName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>distributions</code> resource, the following permissions are required:

### Create
```json
lightsail:AttachCertificateToDistribution,
lightsail:CreateDistribution,
lightsail:DetachCertificateFromDistribution,
lightsail:GetCertificates,
lightsail:GetCertificateDetails,
lightsail:GetDistributions,
lightsail:TagResource,
lightsail:UntagResource,
lightsail:UpdateDistribution,
lightsail:UpdateDistributionBundle
```

### Delete
```json
lightsail:DeleteDistribution,
lightsail:GetDistributions
```

### List
```json
lightsail:GetDistributions
```

