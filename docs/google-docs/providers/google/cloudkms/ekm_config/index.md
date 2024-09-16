---
title: ekm_config
hide_title: false
hide_table_of_contents: false
keywords:
  - ekm_config
  - cloudkms
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

Creates, updates, deletes, gets or lists a <code>ekm_config</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>ekm_config</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.cloudkms.ekm_config" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The resource name for the EkmConfig in the format `projects/*/locations/*/ekmConfig`. |
| <CopyableCode code="defaultEkmConnection" /> | `string` | Optional. Resource name of the default EkmConnection. Setting this field to the empty string removes the default. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_ekm_config" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Returns the EkmConfig singleton resource for a given project and location. |
| <CopyableCode code="update_ekm_config" /> | `UPDATE` | <CopyableCode code="locationsId, projectsId" /> | Updates the EkmConfig singleton resource for a given project and location. |

## `SELECT` examples

Returns the EkmConfig singleton resource for a given project and location.

```sql
SELECT
name,
defaultEkmConnection
FROM google.cloudkms.ekm_config
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `UPDATE` example

Updates a <code>ekm_config</code> resource.

```sql
/*+ update */
UPDATE google.cloudkms.ekm_config
SET 
defaultEkmConnection = '{{ defaultEkmConnection }}'
WHERE 
locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
