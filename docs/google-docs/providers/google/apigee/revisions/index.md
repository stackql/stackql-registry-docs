---
title: revisions
hide_title: false
hide_table_of_contents: false
keywords:
  - revisions
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

Creates, updates, deletes, gets or lists a <code>revisions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>revisions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.apigee.revisions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="contentType" /> | `string` | The HTTP Content-Type header value specifying the content type of the body. |
| <CopyableCode code="data" /> | `string` | The HTTP request/response body as raw binary. |
| <CopyableCode code="extensions" /> | `array` | Application specific response metadata. Must be set in the first response for streaming APIs. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="organizations_apis_revisions_get" /> | `SELECT` | <CopyableCode code="apisId, organizationsId, revisionsId" /> | Gets an API proxy revision. To download the API proxy configuration bundle for the specified revision as a zip file, set the `format` query parameter to `bundle`. If you are using curl, specify `-o filename.zip` to save the output to a file; otherwise, it displays to `stdout`. Then, develop the API proxy configuration locally and upload the updated API proxy configuration revision, as described in [updateApiProxyRevision](updateApiProxyRevision). |
| <CopyableCode code="organizations_sharedflows_revisions_get" /> | `SELECT` | <CopyableCode code="organizationsId, revisionsId, sharedflowsId" /> | Gets a revision of a shared flow. To download the shared flow configuration bundle for the specified revision as a zip file, set the `format` query parameter to `bundle`. If you are using curl, specify `-o filename.zip` to save the output to a file; otherwise, it displays to `stdout`. Then, develop the shared flow configuration locally and upload the updated sharedFlow configuration revision, as described in [updateSharedFlowRevision](updateSharedFlowRevision). |
| <CopyableCode code="organizations_apis_revisions_delete" /> | `DELETE` | <CopyableCode code="apisId, organizationsId, revisionsId" /> | Deletes an API proxy revision and all policies, resources, endpoints, and revisions associated with it. The API proxy revision must be undeployed before you can delete it. |
| <CopyableCode code="organizations_sharedflows_revisions_delete" /> | `DELETE` | <CopyableCode code="organizationsId, revisionsId, sharedflowsId" /> | Deletes a shared flow and all associated policies, resources, and revisions. You must undeploy the shared flow before deleting it. |
| <CopyableCode code="organizations_environments_apis_revisions_deploy" /> | `EXEC` | <CopyableCode code="apisId, environmentsId, organizationsId, revisionsId" /> | Deploys a revision of an API proxy. If another revision of the same API proxy revision is currently deployed, set the `override` parameter to `true` to have this revision replace the currently deployed revision. You cannot invoke an API proxy until it has been deployed to an environment. After you deploy an API proxy revision, you cannot edit it. To edit the API proxy, you must create and deploy a new revision. For a request path `organizations/{org}/environments/{env}/apis/{api}/revisions/{rev}/deployments`, two permissions are required: * `apigee.deployments.create` on the resource `organizations/{org}/environments/{env}` * `apigee.proxyrevisions.deploy` on the resource `organizations/{org}/apis/{api}/revisions/{rev}`  |
| <CopyableCode code="organizations_environments_apis_revisions_undeploy" /> | `EXEC` | <CopyableCode code="apisId, environmentsId, organizationsId, revisionsId" /> | Undeploys an API proxy revision from an environment. For a request path `organizations/{org}/environments/{env}/apis/{api}/revisions/{rev}/deployments`, two permissions are required: * `apigee.deployments.delete` on the resource `organizations/{org}/environments/{env}` * `apigee.proxyrevisions.undeploy` on the resource `organizations/{org}/apis/{api}/revisions/{rev}` |
| <CopyableCode code="organizations_environments_sharedflows_revisions_deploy" /> | `EXEC` | <CopyableCode code="environmentsId, organizationsId, revisionsId, sharedflowsId" /> | Deploys a revision of a shared flow. If another revision of the same shared flow is currently deployed, set the `override` parameter to `true` to have this revision replace the currently deployed revision. You cannot use a shared flow until it has been deployed to an environment. For a request path `organizations/{org}/environments/{env}/sharedflows/{sf}/revisions/{rev}/deployments`, two permissions are required: * `apigee.deployments.create` on the resource `organizations/{org}/environments/{env}` * `apigee.sharedflowrevisions.deploy` on the resource `organizations/{org}/sharedflows/{sf}/revisions/{rev}` |
| <CopyableCode code="organizations_environments_sharedflows_revisions_undeploy" /> | `EXEC` | <CopyableCode code="environmentsId, organizationsId, revisionsId, sharedflowsId" /> | Undeploys a shared flow revision from an environment. For a request path `organizations/{org}/environments/{env}/sharedflows/{sf}/revisions/{rev}/deployments`, two permissions are required: * `apigee.deployments.delete` on the resource `organizations/{org}/environments/{env}` * `apigee.sharedflowrevisions.undeploy` on the resource `organizations/{org}/sharedflows/{sf}/revisions/{rev}` |

## `SELECT` examples

Gets an API proxy revision. To download the API proxy configuration bundle for the specified revision as a zip file, set the `format` query parameter to `bundle`. If you are using curl, specify `-o filename.zip` to save the output to a file; otherwise, it displays to `stdout`. Then, develop the API proxy configuration locally and upload the updated API proxy configuration revision, as described in [updateApiProxyRevision](updateApiProxyRevision).

```sql
SELECT
contentType,
data,
extensions
FROM google.apigee.revisions
WHERE apisId = '{{ apisId }}'
AND organizationsId = '{{ organizationsId }}'
AND revisionsId = '{{ revisionsId }}';
```

## `DELETE` example

Deletes the specified <code>revisions</code> resource.

```sql
/*+ delete */
DELETE FROM google.apigee.revisions
WHERE apisId = '{{ apisId }}'
AND organizationsId = '{{ organizationsId }}'
AND revisionsId = '{{ revisionsId }}';
```
