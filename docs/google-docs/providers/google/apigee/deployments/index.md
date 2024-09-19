---
title: deployments
hide_title: false
hide_table_of_contents: false
keywords:
  - deployments
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

Creates, updates, deletes, gets or lists a <code>deployments</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>deployments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.apigee.deployments" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="deployments" /> | `array` | List of deployments. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="organizations_apis_deployments_list" /> | `SELECT` | <CopyableCode code="apisId, organizationsId" /> | Lists all deployments of an API proxy. |
| <CopyableCode code="organizations_apis_revisions_deployments_list" /> | `SELECT` | <CopyableCode code="apisId, organizationsId, revisionsId" /> | Lists all deployments of an API proxy revision. |
| <CopyableCode code="organizations_deployments_list" /> | `SELECT` | <CopyableCode code="organizationsId" /> | Lists all deployments of API proxies or shared flows. |
| <CopyableCode code="organizations_environments_apis_deployments_list" /> | `SELECT` | <CopyableCode code="apisId, environmentsId, organizationsId" /> | Lists all deployments of an API proxy in an environment. |
| <CopyableCode code="organizations_environments_deployments_get" /> | `SELECT` | <CopyableCode code="deploymentsId, environmentsId, organizationsId" /> | Gets a particular deployment of Api proxy or a shared flow in an environment |
| <CopyableCode code="organizations_environments_deployments_list" /> | `SELECT` | <CopyableCode code="environmentsId, organizationsId" /> | Lists all deployments of API proxies or shared flows in an environment. |
| <CopyableCode code="organizations_environments_sharedflows_deployments_list" /> | `SELECT` | <CopyableCode code="environmentsId, organizationsId, sharedflowsId" /> | Lists all deployments of a shared flow in an environment. |
| <CopyableCode code="organizations_sharedflows_deployments_list" /> | `SELECT` | <CopyableCode code="organizationsId, sharedflowsId" /> | Lists all deployments of a shared flow. |
| <CopyableCode code="organizations_sharedflows_revisions_deployments_list" /> | `SELECT` | <CopyableCode code="organizationsId, revisionsId, sharedflowsId" /> | Lists all deployments of a shared flow revision. |
| <CopyableCode code="organizations_environments_apis_revisions_deployments_generate_deploy_change_report" /> | `EXEC` | <CopyableCode code="apisId, environmentsId, organizationsId, revisionsId" /> | Generates a report for a dry run analysis of a DeployApiProxy request without committing the deployment. In addition to the standard validations performed when adding deployments, additional analysis will be done to detect possible traffic routing changes that would result from this deployment being created. Any potential routing conflicts or unsafe changes will be reported in the response. This routing analysis is not performed for a non-dry-run DeployApiProxy request. For a request path `organizations/{org}/environments/{env}/apis/{api}/revisions/{rev}/deployments:generateDeployChangeReport`, two permissions are required: * `apigee.deployments.create` on the resource `organizations/{org}/environments/{env}` * `apigee.proxyrevisions.deploy` on the resource `organizations/{org}/apis/{api}/revisions/{rev}` |
| <CopyableCode code="organizations_environments_apis_revisions_deployments_generate_undeploy_change_report" /> | `EXEC` | <CopyableCode code="apisId, environmentsId, organizationsId, revisionsId" /> | Generates a report for a dry run analysis of an UndeployApiProxy request without committing the undeploy. In addition to the standard validations performed when removing deployments, additional analysis will be done to detect possible traffic routing changes that would result from this deployment being removed. Any potential routing conflicts or unsafe changes will be reported in the response. This routing analysis is not performed for a non-dry-run UndeployApiProxy request. For a request path `organizations/{org}/environments/{env}/apis/{api}/revisions/{rev}/deployments:generateUndeployChangeReport`, two permissions are required: * `apigee.deployments.delete` on the resource `organizations/{org}/environments/{env}` * `apigee.proxyrevisions.undeploy` on the resource `organizations/{org}/apis/{api}/revisions/{rev}` |

## `SELECT` examples

Lists all deployments of API proxies or shared flows.

```sql
SELECT
deployments
FROM google.apigee.deployments
WHERE organizationsId = '{{ organizationsId }}';
```
