---
title: configuration_set
hide_title: false
hide_table_of_contents: false
keywords:
  - configuration_set
  - ses
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


Gets or updates an individual <code>configuration_set</code> resource, use <code>configuration_sets</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>configuration_set</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::SES::ConfigurationSet.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ses.configuration_set" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the configuration set.</td></tr>
<tr><td><CopyableCode code="tracking_options" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="delivery_options" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="reputation_options" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="sending_options" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="suppression_options" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="vdm_options" /></td><td><code>object</code></td><td></td></tr>
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
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
name,
tracking_options,
delivery_options,
reputation_options,
sending_options,
suppression_options,
vdm_options
FROM aws.ses.configuration_set
WHERE region = 'us-east-1' AND data__Identifier = '<Name>';
```


## Permissions

To operate on the <code>configuration_set</code> resource, the following permissions are required:

### Read
```json
ses:GetConfigurationSet,
ses:DescribeConfigurationSet
```

### Update
```json
ses:PutConfigurationSetTrackingOptions,
ses:PutConfigurationSetDeliveryOptions,
ses:PutConfigurationSetReputationOptions,
ses:PutConfigurationSetSendingOptions,
ses:PutConfigurationSetSuppressionOptions,
ses:PutConfigurationSetVdmOptions
```

