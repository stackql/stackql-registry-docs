---
title: accounts_file_upload_urls
hide_title: false
hide_table_of_contents: false
keywords:
  - accounts_file_upload_urls
  - test_base
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

Creates, updates, deletes, gets or lists a <code>accounts_file_upload_urls</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>accounts_file_upload_urls</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.test_base.accounts_file_upload_urls" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="blobPath" /> | `string` | The blob path of the uploaded package. It will be used as the 'blobPath' property of PackageResource. |
| <CopyableCode code="uploadUrl" /> | `string` | The URL used for uploading the package. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, testBaseAccountName" /> | Gets the file upload URL of a Test Base Account. |

## `SELECT` examples

Gets the file upload URL of a Test Base Account.


```sql
SELECT
blobPath,
uploadUrl
FROM azure_extras.test_base.accounts_file_upload_urls
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND testBaseAccountName = '{{ testBaseAccountName }}';
```