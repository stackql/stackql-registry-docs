---
title: fhir_datastore_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - fhir_datastore_tags
  - healthlake
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

Expands all tag keys and values for <code>fhir_datastores</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>fhir_datastore_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>HealthLake FHIR Datastore</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.healthlake.fhir_datastore_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="created_at" /></td><td><code>object</code></td><td>The time that a Data Store was created.</td></tr>
<tr><td><CopyableCode code="datastore_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name used in the creation of the Data Store.</td></tr>
<tr><td><CopyableCode code="datastore_endpoint" /></td><td><code>string</code></td><td>The AWS endpoint for the Data Store. Each Data Store will have it's own endpoint with Data Store ID in the endpoint URL.</td></tr>
<tr><td><CopyableCode code="datastore_id" /></td><td><code>string</code></td><td>The AWS-generated ID number for the Data Store.</td></tr>
<tr><td><CopyableCode code="datastore_name" /></td><td><code>string</code></td><td>The user-generated name for the Data Store.</td></tr>
<tr><td><CopyableCode code="datastore_status" /></td><td><code>string</code></td><td>The status of the Data Store. Possible statuses are 'CREATING', 'ACTIVE', 'DELETING', or 'DELETED'.</td></tr>
<tr><td><CopyableCode code="datastore_type_version" /></td><td><code>string</code></td><td>The FHIR version. Only R4 version data is supported.</td></tr>
<tr><td><CopyableCode code="preload_data_config" /></td><td><code>object</code></td><td>The preloaded data configuration for the Data Store. Only data preloaded from Synthea is supported.</td></tr>
<tr><td><CopyableCode code="sse_configuration" /></td><td><code>object</code></td><td>The server-side encryption key configuration for a customer provided encryption key.</td></tr>
<tr><td><CopyableCode code="identity_provider_configuration" /></td><td><code>object</code></td><td>The identity provider configuration for the datastore</td></tr>
<tr><td><CopyableCode code="tag_key" /></td><td><code>string</code></td><td>Tag key.</td></tr>
<tr><td><CopyableCode code="tag_value" /></td><td><code>string</code></td><td>Tag value.</td></tr>
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
Expands tags for all <code>fhir_datastores</code> in a region.
```sql
SELECT
region,
created_at,
datastore_arn,
datastore_endpoint,
datastore_id,
datastore_name,
datastore_status,
datastore_type_version,
preload_data_config,
sse_configuration,
identity_provider_configuration,
tag_key,
tag_value
FROM aws.healthlake.fhir_datastore_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>fhir_datastore_tags</code> resource, see <a href="/providers/aws/healthlake/fhir_datastores/#permissions"><code>fhir_datastores</code></a>

