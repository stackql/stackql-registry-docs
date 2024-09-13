
---
title: sql_integrations
hide_title: false
hide_table_of_contents: false
keywords:
  - sql_integrations
  - managedidentities
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

Creates, updates, deletes or gets an <code>sql_integration</code> resource or lists <code>sql_integrations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sql_integrations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.managedidentities.sql_integrations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The unique name of the SQL integration in the form of `projects/{project_id}/locations/global/domains/{domain_name}/sqlIntegrations/{sql_integration}` |
| <CopyableCode code="createTime" /> | `string` | Output only. The time the SQL integration was created. |
| <CopyableCode code="sqlInstance" /> | `string` | The full resource name of an integrated SQL instance |
| <CopyableCode code="state" /> | `string` | Output only. The current state of the SQL integration. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The time the SQL integration was updated. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="domainsId, projectsId, sqlIntegrationsId" /> | Gets details of a single sqlIntegration. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="domainsId, projectsId" /> | Lists SqlIntegrations in a given domain. |

## `SELECT` examples

Lists SqlIntegrations in a given domain.

```sql
SELECT
name,
createTime,
sqlInstance,
state,
updateTime
FROM google.managedidentities.sql_integrations
WHERE domainsId = '{{ domainsId }}'
AND projectsId = '{{ projectsId }}'; 
```
