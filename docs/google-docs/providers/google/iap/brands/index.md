---
title: brands
hide_title: false
hide_table_of_contents: false
keywords:
  - brands
  - iap
  - google
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>brands</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>brands</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.iap.brands" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. Identifier of the brand. NOTE: GCP project number achieves the same brand identification purpose as only one brand per project can be created. |
| <CopyableCode code="applicationTitle" /> | `string` | Application name displayed on OAuth consent screen. |
| <CopyableCode code="orgInternalOnly" /> | `boolean` | Output only. Whether the brand is only intended for usage inside the G Suite organization only. |
| <CopyableCode code="supportEmail" /> | `string` | Support email displayed on the OAuth consent screen. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="brandsId, projectsId" /> | Retrieves the OAuth brand of the project. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="projectsId" /> | Lists the existing brands for the project. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="projectsId" /> | Constructs a new OAuth brand for the project if one does not exist. The created brand is "internal only", meaning that OAuth clients created under it only accept requests from users who belong to the same Google Workspace organization as the project. The brand is created in an un-reviewed status. NOTE: The "internal only" status can be manually changed in the Google Cloud Console. Requires that a brand does not already exist for the project, and that the specified support email is owned by the caller. |

## `SELECT` examples

Lists the existing brands for the project.

```sql
SELECT
name,
applicationTitle,
orgInternalOnly,
supportEmail
FROM google.iap.brands
WHERE projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>brands</code> resource.

<Tabs
    defaultValue="all"
    values={[
        { label: 'All Properties', value: 'all', },
        { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO google.iap.brands (
projectsId,
name,
supportEmail,
applicationTitle,
orgInternalOnly
)
SELECT 
'{{ projectsId }}',
'{{ name }}',
'{{ supportEmail }}',
'{{ applicationTitle }}',
true|false
;
```
</TabItem>
<TabItem value="manifest">

```yaml
resources:
  - name: instance
    props:
      - name: name
        value: '{{ name }}'
      - name: supportEmail
        value: '{{ supportEmail }}'
      - name: applicationTitle
        value: '{{ applicationTitle }}'
      - name: orgInternalOnly
        value: '{{ orgInternalOnly }}'

```
</TabItem>
</Tabs>
