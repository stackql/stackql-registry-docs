---
title: organization_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - organization_settings
  - securitycenter
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

Creates, updates, deletes, gets or lists a <code>organization_settings</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>organization_settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.securitycenter.organization_settings" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The relative resource name of the settings. See: https://cloud.google.com/apis/design/resource_names#relative_resource_name Example: "organizations/{organization_id}/organizationSettings". |
| <CopyableCode code="assetDiscoveryConfig" /> | `object` | The configuration used for Asset Discovery runs. |
| <CopyableCode code="enableAssetDiscovery" /> | `boolean` | A flag that indicates if Asset Discovery should be enabled. If the flag is set to `true`, then discovery of assets will occur. If it is set to `false`, all historical assets will remain, but discovery of future assets will not occur. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="organizations_get_organization_settings" /> | `SELECT` | <CopyableCode code="organizationsId" /> | Gets the settings for an organization. |
| <CopyableCode code="organizations_update_organization_settings" /> | `UPDATE` | <CopyableCode code="organizationsId" /> | Updates an organization's settings. |

## `SELECT` examples

Gets the settings for an organization.

```sql
SELECT
name,
assetDiscoveryConfig,
enableAssetDiscovery
FROM google.securitycenter.organization_settings
WHERE organizationsId = '{{ organizationsId }}'; 
```

## `UPDATE` example

Updates a <code>organization_settings</code> resource.

```sql
/*+ update */
UPDATE google.securitycenter.organization_settings
SET 
name = '{{ name }}',
enableAssetDiscovery = true|false,
assetDiscoveryConfig = '{{ assetDiscoveryConfig }}'
WHERE 
organizationsId = '{{ organizationsId }}';
```
