---
title: application_detail_service_apk_details
hide_title: false
hide_table_of_contents: false
keywords:
  - application_detail_service_apk_details
  - testing
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

Creates, updates, deletes, gets or lists a <code>application_detail_service_apk_details</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>application_detail_service_apk_details</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.testing.application_detail_service_apk_details" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="apkDetail" /> | `object` | Android application details based on application manifest and archive contents. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_apk_details" /> | `SELECT` | <CopyableCode code="" /> | Gets the details of an Android application APK. |

## `SELECT` examples

Gets the details of an Android application APK.

```sql
SELECT
apkDetail
FROM google.testing.application_detail_service_apk_details
;
```
