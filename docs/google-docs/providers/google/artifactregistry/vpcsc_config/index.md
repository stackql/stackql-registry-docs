---
title: vpcsc_config
hide_title: false
hide_table_of_contents: false
keywords:
  - vpcsc_config
  - artifactregistry
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

Creates, updates, deletes, gets or lists a <code>vpcsc_config</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vpcsc_config</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.artifactregistry.vpcsc_config" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The name of the project's VPC SC Config. Always of the form: projects/{projectID}/locations/{location}/vpcscConfig In update request: never set In response: always set |
| <CopyableCode code="vpcscPolicy" /> | `string` | The project per location VPC SC policy that defines the VPC SC behavior for the Remote Repository (Allow/Deny). |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_vpcsc_config" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Retrieves the VPCSC Config for the Project. |
| <CopyableCode code="update_vpcsc_config" /> | `UPDATE` | <CopyableCode code="locationsId, projectsId" /> | Updates the VPCSC Config for the Project. |

## `SELECT` examples

Retrieves the VPCSC Config for the Project.

```sql
SELECT
name,
vpcscPolicy
FROM google.artifactregistry.vpcsc_config
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `UPDATE` example

Updates a <code>vpcsc_config</code> resource.

```sql
/*+ update */
UPDATE google.artifactregistry.vpcsc_config
SET 
name = '{{ name }}',
vpcscPolicy = '{{ vpcscPolicy }}'
WHERE 
locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
