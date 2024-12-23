---
title: consumer_providers
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - consumer_providers
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

Operations on a <code>consumer_providers</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>consumer_providers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.marketplace.consumer_providers" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="id" /> | `string` |
| <CopyableCode code="name" /> | `string` |
| <CopyableCode code="description" /> | `string` |
| <CopyableCode code="business_contact_email" /> | `string` |
| <CopyableCode code="company_website_link" /> | `string` |
| <CopyableCode code="dark_mode_icon_file_id" /> | `string` |
| <CopyableCode code="dark_mode_icon_file_path" /> | `string` |
| <CopyableCode code="icon_file_id" /> | `string` |
| <CopyableCode code="icon_file_path" /> | `string` |
| <CopyableCode code="is_featured" /> | `boolean` |
| <CopyableCode code="privacy_policy_link" /> | `string` |
| <CopyableCode code="published_by" /> | `string` |
| <CopyableCode code="support_contact_email" /> | `string` |
| <CopyableCode code="term_of_service_link" /> | `string` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="id, deployment_name" /> | Get a provider in the Databricks Marketplace with at least one visible listing. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="deployment_name" /> | List all providers in the Databricks Marketplace with at least one visible listing. |
| <CopyableCode code="batchget" /> | `EXEC` | <CopyableCode code="deployment_name" /> | Batch get a provider in the Databricks Marketplace with at least one visible listing. |

## `SELECT` examples

<Tabs
    defaultValue="list"
    values={[
        { label: 'consumer_providers (list)', value: 'list' },
        { label: 'consumer_providers (get)', value: 'get' }
    ]
}>
<TabItem value="list">

```sql
SELECT
id,
name,
description,
business_contact_email,
company_website_link,
dark_mode_icon_file_id,
dark_mode_icon_file_path,
icon_file_id,
icon_file_path,
is_featured,
privacy_policy_link,
published_by,
support_contact_email,
term_of_service_link
FROM databricks_workspace.marketplace.consumer_providers
WHERE deployment_name = '{{ deployment_name }}';
```

</TabItem>
<TabItem value="get">

```sql
SELECT
id,
name,
description,
business_contact_email,
company_website_link,
dark_mode_icon_file_id,
dark_mode_icon_file_path,
icon_file_id,
icon_file_path,
is_featured,
privacy_policy_link,
published_by,
support_contact_email,
term_of_service_link
FROM databricks_workspace.marketplace.consumer_providers
WHERE id = '{{ id }}' AND
deployment_name = '{{ deployment_name }}';
```

</TabItem>
</Tabs>
