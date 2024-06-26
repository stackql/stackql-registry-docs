---
title: anywhere_caches
hide_title: false
hide_table_of_contents: false
keywords:
  - anywhere_caches
  - storage
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
<tr><td><b>Name</b></td><td><code>anywhere_caches</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.storage.anywhere_caches" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The ID of the resource, including the project number, bucket name and anywhere cache ID. |
| <CopyableCode code="admissionPolicy" /> | `string` | The cache-level entry admission policy. |
| <CopyableCode code="anywhereCacheId" /> | `string` | The ID of the Anywhere cache instance. |
| <CopyableCode code="bucket" /> | `string` | The name of the bucket containing this cache instance. |
| <CopyableCode code="createTime" /> | `string` | The creation time of the cache instance in RFC 3339 format. |
| <CopyableCode code="kind" /> | `string` | The kind of item this is. For Anywhere Cache, this is always storage#anywhereCache. |
| <CopyableCode code="pendingUpdate" /> | `boolean` | True if the cache instance has an active Update long-running operation. |
| <CopyableCode code="selfLink" /> | `string` | The link to this cache instance. |
| <CopyableCode code="state" /> | `string` | The current state of the cache instance. |
| <CopyableCode code="ttl" /> | `string` | The TTL of all cache entries in whole seconds. e.g., "7200s".  |
| <CopyableCode code="updateTime" /> | `string` | The modification time of the cache instance metadata in RFC 3339 format. |
| <CopyableCode code="zone" /> | `string` | The zone in which the cache instance is running. For example, us-central1-a. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="anywhereCacheId, bucket" /> | Returns the metadata of an Anywhere Cache instance. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="bucket" /> | Returns a list of Anywhere Cache instances of the bucket matching the criteria. |
| <CopyableCode code="insert" /> | `INSERT` | <CopyableCode code="bucket" /> | Creates an Anywhere Cache instance. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="anywhereCacheId, bucket" /> | Updates the config(ttl and admissionPolicy) of an Anywhere Cache instance. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="bucket" /> | Returns a list of Anywhere Cache instances of the bucket matching the criteria. |
| <CopyableCode code="disable" /> | `EXEC` | <CopyableCode code="anywhereCacheId, bucket" /> | Disables an Anywhere Cache instance. |
| <CopyableCode code="pause" /> | `EXEC` | <CopyableCode code="anywhereCacheId, bucket" /> | Pauses an Anywhere Cache instance. |
| <CopyableCode code="resume" /> | `EXEC` | <CopyableCode code="anywhereCacheId, bucket" /> | Resumes a paused or disabled Anywhere Cache instance. |
