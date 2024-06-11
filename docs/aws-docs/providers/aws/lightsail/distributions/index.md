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

Creates, updates, deletes or gets a <code>distribution</code> resource or lists <code>distributions</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>distributions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Lightsail::Distribution</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.lightsail.distributions" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="distribution_name" /></td><td><code>string</code></td><td>The name for the distribution.</td></tr>
<tr><td><CopyableCode code="distribution_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="bundle_id" /></td><td><code>string</code></td><td>The bundle ID to use for the distribution.</td></tr>
<tr><td><CopyableCode code="ip_address_type" /></td><td><code>string</code></td><td>The IP address type for the distribution.</td></tr>
<tr><td><CopyableCode code="cache_behaviors" /></td><td><code>array</code></td><td>An array of objects that describe the per-path cache behavior for the distribution.</td></tr>
<tr><td><CopyableCode code="cache_behavior_settings" /></td><td><code>object</code></td><td>An object that describes the cache behavior settings for the distribution.</td></tr>
<tr><td><CopyableCode code="default_cache_behavior" /></td><td><code>object</code></td><td>An object that describes the default cache behavior for the distribution.</td></tr>
<tr><td><CopyableCode code="origin" /></td><td><code>object</code></td><td>An object that describes the origin resource for the distribution, such as a Lightsail instance or load balancer.</td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td>The status of the distribution.</td></tr>
<tr><td><CopyableCode code="able_to_update_bundle" /></td><td><code>boolean</code></td><td>Indicates whether the bundle that is currently applied to your distribution, specified using the distributionName parameter, can be changed to another bundle.</td></tr>
<tr><td><CopyableCode code="is_enabled" /></td><td><code>boolean</code></td><td>Indicates whether the distribution is enabled.</td></tr>
<tr><td><CopyableCode code="certificate_name" /></td><td><code>string</code></td><td>The certificate attached to the Distribution.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
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
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
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
List all <code>distributions</code> in a region.
```sql
SELECT
region,
distribution_name
FROM aws.lightsail.distributions
WHERE region = 'us-east-1';
```
Gets all properties from a <code>distribution</code>.
```sql
SELECT
region,
distribution_name,
distribution_arn,
bundle_id,
ip_address_type,
cache_behaviors,
cache_behavior_settings,
default_cache_behavior,
origin,
status,
able_to_update_bundle,
is_enabled,
certificate_name,
tags
FROM aws.lightsail.distributions
WHERE region = 'us-east-1' AND data__Identifier = '<DistributionName>';
```


## `INSERT` example

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

## `DELETE` example

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

### Read
```json
lightsail:GetDistributions
```

### Update
```json
lightsail:AttachCertificateToDistribution,
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

