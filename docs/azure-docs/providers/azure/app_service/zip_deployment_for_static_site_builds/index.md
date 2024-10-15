---
title: zip_deployment_for_static_site_builds
hide_title: false
hide_table_of_contents: false
keywords:
  - zip_deployment_for_static_site_builds
  - app_service
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

Creates, updates, deletes, gets or lists a <code>zip_deployment_for_static_site_builds</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>zip_deployment_for_static_site_builds</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.app_service.zip_deployment_for_static_site_builds" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="environmentName, name, resourceGroupName, subscriptionId" /> | Description for Deploys zipped content to a specific environment of a static site. |

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>zip_deployment_for_static_site_builds</code> resource.

<Tabs
    defaultValue="all"
    values={[
        { label: 'All Properties', value: 'all', },
        { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO azure.app_service.zip_deployment_for_static_site_builds (
environmentName,
name,
resourceGroupName,
subscriptionId,
kind,
properties
)
SELECT 
'{{ environmentName }}',
'{{ name }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ kind }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: id
      value: string
    - name: name
      value: string
    - name: kind
      value: string
    - name: type
      value: string
    - name: properties
      value:
        - name: appZipUrl
          value: string
        - name: apiZipUrl
          value: string
        - name: deploymentTitle
          value: string
        - name: provider
          value: string
        - name: functionLanguage
          value: string

```
</TabItem>
</Tabs>
