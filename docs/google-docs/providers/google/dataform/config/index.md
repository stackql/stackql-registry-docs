---
title: config
hide_title: false
hide_table_of_contents: false
keywords:
  - config
  - dataform
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

Creates, updates, deletes, gets or lists a <code>config</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>config</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.dataform.config" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Identifier. The config name. |
| <CopyableCode code="defaultKmsKeyName" /> | `string` | Optional. The default KMS key that is used if no encryption key is provided when a repository is created. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_config" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Get default config for a given project and location. |
| <CopyableCode code="update_config" /> | `UPDATE` | <CopyableCode code="locationsId, projectsId" /> | Update default config for a given project and location. |

## `SELECT` examples

Get default config for a given project and location.

```sql
SELECT
name,
defaultKmsKeyName
FROM google.dataform.config
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `UPDATE` example

Updates a <code>config</code> resource.

```sql
/*+ update */
UPDATE google.dataform.config
SET 
name = '{{ name }}',
defaultKmsKeyName = '{{ defaultKmsKeyName }}'
WHERE 
locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
