---
title: crawled_urls
hide_title: false
hide_table_of_contents: false
keywords:
  - crawled_urls
  - websecurityscanner
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

Creates, updates, deletes, gets or lists a <code>crawled_urls</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>crawled_urls</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.websecurityscanner.crawled_urls" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="body" /> | `string` | Output only. The body of the request that was used to visit the URL. |
| <CopyableCode code="httpMethod" /> | `string` | Output only. The http method of the request that was used to visit the URL, in uppercase. |
| <CopyableCode code="url" /> | `string` | Output only. The URL that was crawled. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="projectsId, scanConfigsId, scanRunsId" /> | List CrawledUrls under a given ScanRun. |

## `SELECT` examples

List CrawledUrls under a given ScanRun.

```sql
SELECT
body,
httpMethod,
url
FROM google.websecurityscanner.crawled_urls
WHERE projectsId = '{{ projectsId }}'
AND scanConfigsId = '{{ scanConfigsId }}'
AND scanRunsId = '{{ scanRunsId }}'; 
```
