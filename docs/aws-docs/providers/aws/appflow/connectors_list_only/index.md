---
title: connectors_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - connectors_list_only
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

Lists <code>connectors</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/connectors/"><code>connectors</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>connectors_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::AppFlow::Connector</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.appflow.connectors_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="connector_label" /></td><td><code>string</code></td><td>The name of the connector. The name is unique for each ConnectorRegistration in your AWS account.</td></tr>
<tr><td><CopyableCode code="connector_arn" /></td><td><code>string</code></td><td>The arn of the connector. The arn is unique for each ConnectorRegistration in your AWS account.</td></tr>
<tr><td><CopyableCode code="connector_provisioning_type" /></td><td><code>string</code></td><td>The provisioning type of the connector. Currently the only supported value is LAMBDA.</td></tr>
<tr><td><CopyableCode code="connector_provisioning_config" /></td><td><code>object</code></td><td>Contains information about the configuration of the connector being registered.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>A description about the connector that's being registered.</td></tr>
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
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Lists all <code>connectors</code> in a region.
```sql
SELECT
region,
connector_label
FROM aws.appflow.connectors_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>connectors_list_only</code> resource, see <a href="/providers/aws/appflow/connectors/#permissions"><code>connectors</code></a>


