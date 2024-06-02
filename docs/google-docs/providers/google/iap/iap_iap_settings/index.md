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




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>iap_iap_settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="iap.iap_iap_settings" /></td></tr>
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
| <CopyableCode code="update_iap_settings" /> | `EXEC` | <CopyableCode code="v1Id" /> | Updates the IAP settings on a particular IAP protected resource. It replaces all fields unless the `update_mask` is set. |
