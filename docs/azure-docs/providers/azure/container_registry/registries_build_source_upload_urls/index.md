---
title: registries_build_source_upload_urls
hide_title: false
hide_table_of_contents: false
keywords:
  - registries_build_source_upload_urls
  - container_registry
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

Creates, updates, deletes, gets or lists a <code>registries_build_source_upload_urls</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>registries_build_source_upload_urls</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.container_registry.registries_build_source_upload_urls" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="relativePath" /> | `string` | The relative path to the source. This is used to submit the subsequent queue build request. |
| <CopyableCode code="uploadUrl" /> | `string` | The URL where the client can upload the source. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="registryName, resourceGroupName, subscriptionId" /> | Get the upload location for the user to be able to upload the source. |

## `SELECT` examples

Get the upload location for the user to be able to upload the source.


```sql
SELECT
relativePath,
uploadUrl
FROM azure.container_registry.registries_build_source_upload_urls
WHERE registryName = '{{ registryName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```