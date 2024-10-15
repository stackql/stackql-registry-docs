---
title: test_results_console_log_download_urls
hide_title: false
hide_table_of_contents: false
keywords:
  - test_results_console_log_download_urls
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

Creates, updates, deletes, gets or lists a <code>test_results_console_log_download_urls</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>test_results_console_log_download_urls</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.test_base.test_results_console_log_download_urls" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="downloadUrl" /> | `string` | The download URL. |
| <CopyableCode code="expirationTime" /> | `string` | Expiry date of the download URL. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="packageName, resourceGroupName, subscriptionId, testBaseAccountName, testResultName, data__logFileName" /> | Gets the download URL of the test execution console log file. |

## `SELECT` examples

Gets the download URL of the test execution console log file.


```sql
SELECT
downloadUrl,
expirationTime
FROM azure_extras.test_base.test_results_console_log_download_urls
WHERE packageName = '{{ packageName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND testBaseAccountName = '{{ testBaseAccountName }}'
AND testResultName = '{{ testResultName }}'
AND data__logFileName = '{{ data__logFileName }}';
```