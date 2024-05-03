---
title: namespaces
hide_title: false
hide_table_of_contents: false
keywords:
  - namespaces
  - functions
  - digitalocean    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Sumologic resources using SQL
custom_edit_url: null
image: /img/providers/digitalocean/stackql-digitalocean-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>namespaces</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="digitalocean.functions.namespaces" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="api_host" /> | `string` | The namespace's API hostname. Each function in a namespace is provided an endpoint at the namespace's hostname. |
| <CopyableCode code="created_at" /> | `string` | UTC time string. |
| <CopyableCode code="key" /> | `string` | A random alpha numeric string. This key is used in conjunction with the namespace's UUID to authenticate <br />a user to use the namespace via `doctl`, DigitalOcean's official CLI. |
| <CopyableCode code="label" /> | `string` | The namespace's unique name. |
| <CopyableCode code="namespace" /> | `string` | A unique string format of UUID with a prefix fn-. |
| <CopyableCode code="region" /> | `string` | The namespace's datacenter region. |
| <CopyableCode code="updated_at" /> | `string` | UTC time string. |
| <CopyableCode code="uuid" /> | `string` | The namespace's Universally Unique Identifier. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_namespace" /> | `SELECT` | <CopyableCode code="namespace_id" /> | Gets the namespace details for the given namespace UUID. To get namespace details, send a GET request to `/v2/functions/namespaces/$NAMESPACE_ID` with no parameters. |
| <CopyableCode code="list_namespaces" /> | `SELECT` |  | Returns a list of namespaces associated with the current user. To get all namespaces, send a GET request to `/v2/functions/namespaces`. |
| <CopyableCode code="create_namespace" /> | `INSERT` | <CopyableCode code="data__label, data__region" /> | Creates a new serverless functions namespace in the desired region and associates it with the provided label. A namespace is a collection of functions and their associated packages, triggers, and project specifications. To create a namespace, send a POST request to `/v2/functions/namespaces` with the `region` and `label` properties. |
| <CopyableCode code="delete_namespace" /> | `DELETE` | <CopyableCode code="namespace_id" /> | Deletes the given namespace.  When a namespace is deleted all assets, in the namespace are deleted, this includes packages, functions and triggers. Deleting a namespace is a destructive operation and assets in the namespace are not recoverable after deletion. Some metadata is retained, such as activations, or soft deleted for reporting purposes.<br />To delete namespace, send a DELETE request to `/v2/functions/namespaces/$NAMESPACE_ID`.<br />A successful deletion returns a 204 response. |
| <CopyableCode code="_get_namespace" /> | `EXEC` | <CopyableCode code="namespace_id" /> | Gets the namespace details for the given namespace UUID. To get namespace details, send a GET request to `/v2/functions/namespaces/$NAMESPACE_ID` with no parameters. |
| <CopyableCode code="_list_namespaces" /> | `EXEC` |  | Returns a list of namespaces associated with the current user. To get all namespaces, send a GET request to `/v2/functions/namespaces`. |
