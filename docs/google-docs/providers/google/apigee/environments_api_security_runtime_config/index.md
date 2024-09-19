---
title: environments_api_security_runtime_config
hide_title: false
hide_table_of_contents: false
keywords:
  - environments_api_security_runtime_config
  - apigee
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

Creates, updates, deletes, gets or lists a <code>environments_api_security_runtime_config</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>environments_api_security_runtime_config</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.apigee.environments_api_security_runtime_config" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Name of the environment API Security Runtime configuration resource. Format: `organizations/{org}/environments/{env}/apiSecurityRuntimeConfig` |
| <CopyableCode code="location" /> | `array` | A list of up to 5 Cloud Storage Blobs that contain SecurityActions. |
| <CopyableCode code="revisionId" /> | `string` | Revision ID of the API Security Runtime configuration. The higher the value, the more recently the configuration was deployed. |
| <CopyableCode code="uid" /> | `string` | Unique ID for the API Security Runtime configuration. The ID will only change if the environment is deleted and recreated. |
| <CopyableCode code="updateTime" /> | `string` | Time that the API Security Runtime configuration was updated. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="organizations_environments_get_api_security_runtime_config" /> | `SELECT` | <CopyableCode code="environmentsId, organizationsId" /> | Gets the API Security runtime configuration for an environment. This named ApiSecurityRuntimeConfig to prevent conflicts with ApiSecurityConfig from addon config. |

## `SELECT` examples

Gets the API Security runtime configuration for an environment. This named ApiSecurityRuntimeConfig to prevent conflicts with ApiSecurityConfig from addon config.

```sql
SELECT
name,
location,
revisionId,
uid,
updateTime
FROM google.apigee.environments_api_security_runtime_config
WHERE environmentsId = '{{ environmentsId }}'
AND organizationsId = '{{ organizationsId }}';
```
