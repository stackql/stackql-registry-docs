---
title: published_apps
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - published_apps
  - oauth
  - databricks_account
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Databricks resources using SQL
custom_edit_url: null
image: /img/providers/databricks_account/stackql-databricks-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Operations on a <code>published_apps</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>published_apps</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_account.oauth.published_apps" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="name" /> | `string` |
| <CopyableCode code="description" /> | `string` |
| <CopyableCode code="app_id" /> | `string` |
| <CopyableCode code="client_id" /> | `string` |
| <CopyableCode code="is_confidential_client" /> | `boolean` |
| <CopyableCode code="redirect_urls" /> | `array` |
| <CopyableCode code="scopes" /> | `array` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="account_id" /> | Get all the available published OAuth apps in Databricks. |

## `SELECT` examples

```sql
SELECT
name,
description,
app_id,
client_id,
is_confidential_client,
redirect_urls,
scopes
FROM databricks_account.oauth.published_apps
WHERE account_id = '{{ account_id }}';
```
