---
title: configuration_aggregator
hide_title: false
hide_table_of_contents: false
keywords:
  - configuration_aggregator
  - config
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

Gets or operates on an individual <code>configuration_aggregator</code> resource, use <code>configuration_aggregators</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>configuration_aggregator</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Config::ConfigurationAggregator</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.config.configuration_aggregator" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="account_aggregation_sources" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="configuration_aggregator_name" /></td><td><code>string</code></td><td>The name of the aggregator.</td></tr>
<tr><td><CopyableCode code="configuration_aggregator_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the aggregator.</td></tr>
<tr><td><CopyableCode code="organization_aggregation_source" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>The tags for the configuration aggregator.</td></tr>
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
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
account_aggregation_sources,
configuration_aggregator_name,
configuration_aggregator_arn,
organization_aggregation_source,
tags
FROM aws.config.configuration_aggregator
WHERE data__Identifier = '<ConfigurationAggregatorName>';
```

## Permissions

To operate on the <code>configuration_aggregator</code> resource, the following permissions are required:

### Read
```json
config:DescribeConfigurationAggregators,
config:ListTagsForResource
```

### Update
```json
config:PutConfigurationAggregator,
config:DescribeConfigurationAggregators,
config:TagResource,
config:UntagResource,
config:ListTagsForResource,
iam:PassRole,
organizations:EnableAWSServiceAccess,
organizations:ListDelegatedAdministrators
```

### Delete
```json
config:DeleteConfigurationAggregator,
config:UntagResource
```

