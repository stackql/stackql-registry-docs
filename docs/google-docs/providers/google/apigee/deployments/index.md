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
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>deployments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.apigee.deployments</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `organizations_apis_deployments_list` | `SELECT` | `apisId, organizationsId` | Lists all deployments of an API proxy. |
| `organizations_apis_revisions_deployments_list` | `SELECT` | `apisId, organizationsId, revisionsId` | Lists all deployments of an API proxy revision. |
| `organizations_deployments_list` | `SELECT` | `organizationsId` | Lists all deployments of API proxies or shared flows. |
| `organizations_environments_apis_deployments_list` | `SELECT` | `apisId, environmentsId, organizationsId` | Lists all deployments of an API proxy in an environment. |
| `organizations_environments_deployments_list` | `SELECT` | `environmentsId, organizationsId` | Lists all deployments of API proxies or shared flows in an environment. |
| `organizations_environments_sharedflows_deployments_list` | `SELECT` | `environmentsId, organizationsId, sharedflowsId` | Lists all deployments of a shared flow in an environment. |
| `organizations_sharedflows_deployments_list` | `SELECT` | `organizationsId, sharedflowsId` | Lists all deployments of a shared flow. |
| `organizations_sharedflows_revisions_deployments_list` | `SELECT` | `organizationsId, revisionsId, sharedflowsId` | Lists all deployments of a shared flow revision. |
| `organizations_environments_apis_revisions_deployments_generateDeployChangeReport` | `EXEC` | `apisId, environmentsId, organizationsId, revisionsId` | Generates a report for a dry run analysis of a DeployApiProxy request without committing the deployment. In addition to the standard validations performed when adding deployments, additional analysis will be done to detect possible traffic routing changes that would result from this deployment being created. Any potential routing conflicts or unsafe changes will be reported in the response. This routing analysis is not performed for a non-dry-run DeployApiProxy request. For a request path `organizations/{org}/environments/{env}/apis/{api}/revisions/{rev}/deployments:generateDeployChangeReport`, two permissions are required: * `apigee.deployments.create` on the resource `organizations/{org}/environments/{env}` * `apigee.proxyrevisions.deploy` on the resource `organizations/{org}/apis/{api}/revisions/{rev}` |
| `organizations_environments_apis_revisions_deployments_generateUndeployChangeReport` | `EXEC` | `apisId, environmentsId, organizationsId, revisionsId` | Generates a report for a dry run analysis of an UndeployApiProxy request without committing the undeploy. In addition to the standard validations performed when removing deployments, additional analysis will be done to detect possible traffic routing changes that would result from this deployment being removed. Any potential routing conflicts or unsafe changes will be reported in the response. This routing analysis is not performed for a non-dry-run UndeployApiProxy request. For a request path `organizations/{org}/environments/{env}/apis/{api}/revisions/{rev}/deployments:generateUndeployChangeReport`, two permissions are required: * `apigee.deployments.delete` on the resource `organizations/{org}/environments/{env}` * `apigee.proxyrevisions.undeploy` on the resource `organizations/{org}/apis/{api}/revisions/{rev}` |
