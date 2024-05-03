---
title: artifacts
hide_title: false
hide_table_of_contents: false
keywords:
  - artifacts
  - artifacts
  - vercel    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy, and manage Vercel resources using SQL
custom_edit_url: null
image: /img/providers/vercel/stackql-vercel-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>artifacts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="vercel.artifacts.artifacts" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="artifact_exists" /> | `EXEC` | <CopyableCode code="hash, teamId" /> | Check that a cache artifact with the given `hash` exists. This request returns response headers only and is equivalent to a `GET` request to this endpoint where the response contains no body. |
| <CopyableCode code="artifact_query" /> | `EXEC` | <CopyableCode code="teamId, data__hashes" /> | Query information about an array of artifacts. |
| <CopyableCode code="download_artifact" /> | `EXEC` | <CopyableCode code="hash, teamId" /> | Downloads a cache artifact indentified by its `hash` specified on the request path. The artifact is downloaded as an octet-stream. The client should verify the content-length header and response body. |
| <CopyableCode code="record_events" /> | `EXEC` | <CopyableCode code="teamId" /> | Records an artifacts cache usage event. The body of this request is an array of cache usage events. The supported event types are `HIT` and `MISS`. The source is either `LOCAL` the cache event was on the users filesystem cache or `REMOTE` if the cache event is for a remote cache. When the event is a `HIT` the request also accepts a number `duration` which is the time taken to generate the artifact in the cache. |
| <CopyableCode code="status" /> | `EXEC` | <CopyableCode code="teamId" /> | Check the status of Remote Caching for this principal. Returns a JSON-encoded status indicating if Remote Caching is enabled, disabled, or disabled due to usage limits. |
| <CopyableCode code="upload_artifact" /> | `EXEC` | <CopyableCode code="Content-Length, hash, teamId" /> | Uploads a cache artifact identified by the `hash` specified on the path. The cache artifact can then be downloaded with the provided `hash`. |
