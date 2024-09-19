---
title: iap_iap_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - iap_iap_settings
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

Creates, updates, deletes, gets or lists a <code>iap_iap_settings</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>iap_iap_settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.iap.iap_iap_settings" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Required. The resource name of the IAP protected resource. |
| <CopyableCode code="accessSettings" /> | `object` | Access related settings for IAP protected apps. |
| <CopyableCode code="applicationSettings" /> | `object` | Wrapper over application specific settings for IAP. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_iap_settings" /> | `SELECT` | <CopyableCode code="v1Id" /> | Gets the IAP settings on a particular IAP protected resource. |
| <CopyableCode code="update_iap_settings" /> | `UPDATE` | <CopyableCode code="v1Id" /> | Updates the IAP settings on a particular IAP protected resource. It replaces all fields unless the `update_mask` is set. |

## `SELECT` examples

Gets the IAP settings on a particular IAP protected resource.

```sql
SELECT
name,
accessSettings,
applicationSettings
FROM google.iap.iap_iap_settings
WHERE v1Id = '{{ v1Id }}';
```

## `UPDATE` example

Updates a <code>iap_iap_settings</code> resource.

```sql
/*+ update */
UPDATE google.iap.iap_iap_settings
SET 
name = '{{ name }}',
accessSettings = '{{ accessSettings }}',
applicationSettings = '{{ applicationSettings }}'
WHERE 
v1Id = '{{ v1Id }}';
```
