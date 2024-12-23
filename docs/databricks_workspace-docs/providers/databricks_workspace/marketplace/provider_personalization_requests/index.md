---
title: provider_personalization_requests
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - provider_personalization_requests
  - marketplace
  - databricks_workspace
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Databricks resources using SQL
custom_edit_url: null
image: /img/providers/databricks_workspace/stackql-databricks-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Operations on a <code>provider_personalization_requests</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>provider_personalization_requests</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.marketplace.provider_personalization_requests" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="id" /> | `string` |
| <CopyableCode code="comment" /> | `string` |
| <CopyableCode code="consumer_region" /> | `object` |
| <CopyableCode code="contact_info" /> | `object` |
| <CopyableCode code="created_at" /> | `integer` |
| <CopyableCode code="intended_use" /> | `string` |
| <CopyableCode code="is_from_lighthouse" /> | `boolean` |
| <CopyableCode code="listing_id" /> | `string` |
| <CopyableCode code="listing_name" /> | `string` |
| <CopyableCode code="metastore_id" /> | `string` |
| <CopyableCode code="provider_id" /> | `string` |
| <CopyableCode code="recipient_type" /> | `string` |
| <CopyableCode code="share" /> | `object` |
| <CopyableCode code="status" /> | `string` |
| <CopyableCode code="status_message" /> | `string` |
| <CopyableCode code="updated_at" /> | `integer` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="deployment_name" /> | List personalization requests to this provider. This will return all personalization requests, regardless of which listing they are for. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="listing_id, request_id, deployment_name" /> | Update personalization request. This method only permits updating the status of the request. |

## `SELECT` examples

```sql
SELECT
id,
comment,
consumer_region,
contact_info,
created_at,
intended_use,
is_from_lighthouse,
listing_id,
listing_name,
metastore_id,
provider_id,
recipient_type,
share,
status,
status_message,
updated_at
FROM databricks_workspace.marketplace.provider_personalization_requests
WHERE deployment_name = '{{ deployment_name }}';
```

## `UPDATE` example

Updates a <code>provider_personalization_requests</code> resource.

```sql
/*+ update */
-- replace field1, field2, etc. with the fields you want to update        
UPDATE databricks_workspace.marketplace.provider_personalization_requests
SET field1 = '{{ value1 }}',
field2 = '{{ value2 }}', ...
WHERE listing_id = '{{ listing_id }}' AND
request_id = '{{ request_id }}' AND
deployment_name = '{{ deployment_name }}';
```
