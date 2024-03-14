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
Gets an individual <code>configuration_aggregator</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>configuration_aggregator</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>configuration_aggregator</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.config.configuration_aggregator</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>account_aggregation_sources</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>configuration_aggregator_name</code></td><td><code>string</code></td><td>The name of the aggregator.</td></tr>
<tr><td><code>configuration_aggregator_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the aggregator.</td></tr>
<tr><td><code>organization_aggregation_source</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>The tags for the configuration aggregator.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
account_aggregation_sources,
configuration_aggregator_name,
configuration_aggregator_arn,
organization_aggregation_source,
tags
FROM awscc.config.configuration_aggregator
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

