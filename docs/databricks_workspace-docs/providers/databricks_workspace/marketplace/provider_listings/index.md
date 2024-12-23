---
title: provider_listings
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - provider_listings
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

Operations on a <code>provider_listings</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>provider_listings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.marketplace.provider_listings" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="id" /> | `string` |
| <CopyableCode code="detail" /> | `object` |
| <CopyableCode code="summary" /> | `object` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="id, deployment_name" /> | Get a listing |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="deployment_name" /> | List listings owned by this provider |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="deployment_name" /> | Create a new listing |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="id, deployment_name" /> | Delete a listing |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="id, deployment_name" /> | Update a listing |

## `SELECT` examples

<Tabs
    defaultValue="list"
    values={[
        { label: 'provider_listings (list)', value: 'list' },
        { label: 'provider_listings (get)', value: 'get' }
    ]
}>
<TabItem value="list">

```sql
SELECT
id,
detail,
summary
FROM databricks_workspace.marketplace.provider_listings
WHERE deployment_name = '{{ deployment_name }}';
```

</TabItem>
<TabItem value="get">

```sql
SELECT
id,
detail,
summary
FROM databricks_workspace.marketplace.provider_listings
WHERE id = '{{ id }}' AND
deployment_name = '{{ deployment_name }}';
```

</TabItem>
</Tabs>

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>provider_listings</code> resource.

<Tabs
    defaultValue="create"
    values={[
        { label: 'provider_listings', value: 'create', },
        { label: 'Manifest', value: 'manifest', },
    ]}
>
<TabItem value="create">

```sql
/*+ create */
INSERT INTO databricks_workspace.marketplace.provider_listings (
deployment_name,
data__listing
)
SELECT 
'{{ deployment_name }}',
'{{ listing }}'
;
```

</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
  - name: listing
    value:
      id: string
      summary:
        name: string
        subtitle: string
        status: DRAFT
        share:
          name: string
          type: SAMPLE
        provider_region:
          cloud: string
          region: string
        setting:
          visibility: PUBLIC
        created_at: 0
        created_by: string
        updated_at: 0
        updated_by: string
        published_at: 0
        published_by: string
        categories:
        - ADVERTISING_AND_MARKETING
        listingType: STANDARD
        created_by_id: 0
        updated_by_id: 0
        provider_id: string
        exchange_ids:
        - string
        git_repo:
          git_repo_url: string
      detail:
        description: string
        terms_of_service: string
        documentation_link: string
        support_link: string
        file_ids:
        - string
        privacy_policy_link: string
        embedded_notebook_file_infos:
        - id: string
          marketplace_file_type: PROVIDER_ICON
          file_parent:
            parent_id: string
            file_parent_type: PROVIDER
          mime_type: string
          download_link: string
          created_at: 0
          updated_at: 0
          display_name: string
          status: FILE_STATUS_PUBLISHED
          status_message: string
        geographical_coverage: string
        cost: FREE
        pricing_model: string
        update_frequency:
          interval: 0
          unit: NONE
        collection_granularity:
          interval: 0
          unit: NONE
        collection_date_start: 0
        collection_date_end: 0
        data_source: string
        size: 0.1
        assets:
        - ASSET_TYPE_GIT_REPO
        license: string
        tags:
        - tag_name: LISTING_TAG_TYPE_LANGUAGE
          tag_values:
          - string

```

</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>provider_listings</code> resource.

```sql
/*+ update */
UPDATE databricks_workspace.marketplace.provider_listings
SET { field = value }
WHERE id = '{{ id }}' AND
deployment_name = '{{ deployment_name }}';
```

## `DELETE` example

Deletes a <code>provider_listings</code> resource.

```sql
/*+ delete */
DELETE FROM databricks_workspace.marketplace.provider_listings
WHERE id = '{{ id }}' AND
deployment_name = '{{ deployment_name }}';
```
