---
title: clients
hide_title: false
hide_table_of_contents: false
keywords:
  - clients
  - integrations
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

Creates, updates, deletes, gets or lists a <code>clients</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>clients</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.integrations.clients" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="client" /> | `object` | The configuration information for the Client |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_get_clients" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Gets the client configuration for the given project and location resource name |
| <CopyableCode code="projects_locations_clients_deprovision" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Perform the deprovisioning steps to disable a user GCP project to use IP and purge all related data in a wipeout-compliant way. |
| <CopyableCode code="projects_locations_clients_provision" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Perform the provisioning steps to enable a user GCP project to use IP. If GCP project already registered on IP end via Apigee Integration, provisioning will fail. |
| <CopyableCode code="projects_locations_clients_replace" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Update run-as service account for provisioned client |
| <CopyableCode code="projects_locations_clients_switch" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Update client from GMEK to CMEK |
| <CopyableCode code="projects_locations_clients_switch_variable_masking" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Update variable masking for provisioned client |

## `SELECT` examples

Gets the client configuration for the given project and location resource name

```sql
SELECT
client
FROM google.integrations.clients
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```
