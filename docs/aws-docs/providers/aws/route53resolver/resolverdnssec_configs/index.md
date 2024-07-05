---
title: resolverdnssec_configs
hide_title: false
hide_table_of_contents: false
keywords:
  - resolverdnssec_configs
  - route53resolver
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

Creates, updates, deletes or gets a <code>resolverdnssec_config</code> resource or lists <code>resolverdnssec_configs</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>resolverdnssec_configs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::Route53Resolver::ResolverDNSSECConfig.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.route53resolver.resolverdnssec_configs" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>Id</td></tr>
<tr><td><CopyableCode code="owner_id" /></td><td><code>string</code></td><td>AccountId</td></tr>
<tr><td><CopyableCode code="resource_id" /></td><td><code>string</code></td><td>ResourceId</td></tr>
<tr><td><CopyableCode code="validation_status" /></td><td><code>string</code></td><td>ResolverDNSSECValidationStatus, possible values are ENABLING, ENABLED, DISABLING AND DISABLED.</td></tr>
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
    <td><CopyableCode code="region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
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
Gets all <code>resolverdnssec_configs</code> in a region.
```sql
SELECT
region,
id,
owner_id,
resource_id,
validation_status
FROM aws.route53resolver.resolverdnssec_configs
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>resolverdnssec_config</code>.
```sql
SELECT
region,
id,
owner_id,
resource_id,
validation_status
FROM aws.route53resolver.resolverdnssec_configs
WHERE region = 'us-east-1' AND data__Identifier = '<Id>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>resolverdnssec_config</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.route53resolver.resolverdnssec_configs (
 ResourceId,
 region
)
SELECT 
'{{ ResourceId }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.route53resolver.resolverdnssec_configs (
 ResourceId,
 region
)
SELECT 
 '{{ ResourceId }}',
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
  - name: resolverdnssec_config
    props:
      - name: ResourceId
        value: '{{ ResourceId }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.route53resolver.resolverdnssec_configs
WHERE data__Identifier = '<Id>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>resolverdnssec_configs</code> resource, the following permissions are required:

### Create
```json
resolverdnssec:CreateConfig,
route53resolver:UpdateResolverDnssecConfig,
route53resolver:GetResolverDnssecConfig,
ec2:DescribeVpcs
```

### Read
```json
resolverdnssec:GetConfig,
route53resolver:ListResolverDnssecConfigs
```

### Delete
```json
resolverdnssec:DeleteConfig,
route53resolver:UpdateResolverDnssecConfig,
route53resolver:ListResolverDnssecConfigs,
ec2:DescribeVpcs
```

### List
```json
resolverdnssec:ListConfig,
route53resolver:ListResolverDnssecConfigs
```

