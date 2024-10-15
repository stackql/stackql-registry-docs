---
title: images_upload_url_for_data
hide_title: false
hide_table_of_contents: false
keywords:
  - images_upload_url_for_data
  - customer_insights
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

Creates, updates, deletes, gets or lists a <code>images_upload_url_for_data</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>images_upload_url_for_data</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.customer_insights.images_upload_url_for_data" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="contentUrl" /> | `string` | Content URL for the image blob. |
| <CopyableCode code="imageExists" /> | `boolean` | Whether image exists already. |
| <CopyableCode code="relativePath" /> | `string` | Relative path of the image. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="hubName, resourceGroupName, subscriptionId" /> | Gets data image upload URL. |

## `SELECT` examples

Gets data image upload URL.


```sql
SELECT
contentUrl,
imageExists,
relativePath
FROM azure_extras.customer_insights.images_upload_url_for_data
WHERE hubName = '{{ hubName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```