---
title: build_service_resource_upload_urls
hide_title: false
hide_table_of_contents: false
keywords:
  - build_service_resource_upload_urls
  - spring_apps
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

Creates, updates, deletes, gets or lists a <code>build_service_resource_upload_urls</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>build_service_resource_upload_urls</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.spring_apps.build_service_resource_upload_urls" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="relativePath" /> | `string` | Source relative path |
| <CopyableCode code="uploadUrl" /> | `string` | Upload URL |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="buildServiceName, resourceGroupName, serviceName, subscriptionId" /> | Get an resource upload URL for build service, which may be artifacts or source archive. |

## `SELECT` examples

Get an resource upload URL for build service, which may be artifacts or source archive.


```sql
SELECT
relativePath,
uploadUrl
FROM azure.spring_apps.build_service_resource_upload_urls
WHERE buildServiceName = '{{ buildServiceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```