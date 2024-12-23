---
title: listing_installations
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - listing_installations
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

Operations on a <code>listing_installations</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>listing_installations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.marketplace.listing_installations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="id" /> | `string` |
| <CopyableCode code="catalog_name" /> | `string` |
| <CopyableCode code="error_message" /> | `string` |
| <CopyableCode code="installed_on" /> | `integer` |
| <CopyableCode code="listing_id" /> | `string` |
| <CopyableCode code="listing_name" /> | `string` |
| <CopyableCode code="recipient_type" /> | `string` |
| <CopyableCode code="repo_name" /> | `string` |
| <CopyableCode code="repo_path" /> | `string` |
| <CopyableCode code="share_name" /> | `string` |
| <CopyableCode code="status" /> | `string` |
| <CopyableCode code="token_detail" /> | `object` |
| <CopyableCode code="tokens" /> | `array` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="listlistinginstallations" /> | `SELECT` | <CopyableCode code="listing_id, deployment_name" /> | List all installations for a particular listing. |

## `SELECT` examples

```sql
SELECT
id,
catalog_name,
error_message,
installed_on,
listing_id,
listing_name,
recipient_type,
repo_name,
repo_path,
share_name,
status,
token_detail,
tokens
FROM databricks_workspace.marketplace.listing_installations
WHERE listing_id = '{{ listing_id }}' AND
deployment_name = '{{ deployment_name }}';
```
