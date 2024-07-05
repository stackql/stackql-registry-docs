---
title: resolver_configs
hide_title: false
hide_table_of_contents: false
keywords:
  - resolver_configs
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

Creates, updates, deletes or gets a <code>resolver_config</code> resource or lists <code>resolver_configs</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>resolver_configs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::Route53Resolver::ResolverConfig.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.route53resolver.resolver_configs" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>Id</td></tr>
<tr><td><CopyableCode code="owner_id" /></td><td><code>string</code></td><td>AccountId</td></tr>
<tr><td><CopyableCode code="resource_id" /></td><td><code>string</code></td><td>ResourceId</td></tr>
<tr><td><CopyableCode code="autodefined_reverse" /></td><td><code>string</code></td><td>ResolverAutodefinedReverseStatus, possible values are ENABLING, ENABLED, DISABLING AND DISABLED.</td></tr>
<tr><td><CopyableCode code="autodefined_reverse_flag" /></td><td><code>string</code></td><td>Represents the desired status of AutodefinedReverse. The only supported value on creation is DISABLE. Deletion of this resource will return AutodefinedReverse to its default value (ENABLED).</td></tr>
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
    <td><CopyableCode code="ResourceId, AutodefinedReverseFlag, region" /></td>
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
Gets all <code>resolver_configs</code> in a region.
```sql
SELECT
region,
id,
owner_id,
resource_id,
autodefined_reverse,
autodefined_reverse_flag
FROM aws.route53resolver.resolver_configs
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>resolver_config</code>.
```sql
SELECT
region,
id,
owner_id,
resource_id,
autodefined_reverse,
autodefined_reverse_flag
FROM aws.route53resolver.resolver_configs
WHERE region = 'us-east-1' AND data__Identifier = '<ResourceId>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>resolver_config</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.route53resolver.resolver_configs (
 ResourceId,
 AutodefinedReverseFlag,
 region
)
SELECT 
'{{ ResourceId }}',
 '{{ AutodefinedReverseFlag }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.route53resolver.resolver_configs (
 ResourceId,
 AutodefinedReverseFlag,
 region
)
SELECT 
 '{{ ResourceId }}',
 '{{ AutodefinedReverseFlag }}',
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
  - name: resolver_config
    props:
      - name: ResourceId
        value: '{{ ResourceId }}'
      - name: AutodefinedReverseFlag
        value: '{{ AutodefinedReverseFlag }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.route53resolver.resolver_configs
WHERE data__Identifier = '<ResourceId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>resolver_configs</code> resource, the following permissions are required:

### Create
```json
route53resolver:UpdateResolverConfig,
route53resolver:GetResolverConfig,
ec2:DescribeVpcs
```

### Read
```json
route53resolver:GetResolverConfig,
ec2:DescribeVpcs
```

### Delete
```json
route53resolver:UpdateResolverConfig,
route53resolver:ListResolverConfigs,
ec2:DescribeVpcs
```

### List
```json
route53resolver:ListResolverConfigs,
ec2:DescribeVpcs
```

