---
title: versions
hide_title: false
hide_table_of_contents: false
keywords:
  - versions
  - appengine
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




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.appengine.versions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Relative name of the version within the service. Example: v1. Version names can contain only lowercase letters, numbers, or hyphens. Reserved names: "default", "latest", and any name with the prefix "ah-". |
| <CopyableCode code="name" /> | `string` | Full path to the Version resource in the API. Example: apps/myapp/services/default/versions/v1.@OutputOnly |
| <CopyableCode code="apiConfig" /> | `object` | Google Cloud Endpoints (https://cloud.google.com/endpoints) configuration for API handlers. |
| <CopyableCode code="appEngineApis" /> | `boolean` | Allows App Engine second generation runtimes to access the legacy bundled services. |
| <CopyableCode code="automaticScaling" /> | `object` | Automatic scaling is based on request rate, response latencies, and other application metrics. |
| <CopyableCode code="basicScaling" /> | `object` | A service with basic scaling will create an instance when the application receives a request. The instance will be turned down when the app becomes idle. Basic scaling is ideal for work that is intermittent or driven by user activity. |
| <CopyableCode code="betaSettings" /> | `object` | Metadata settings that are supplied to this version to enable beta runtime features. |
| <CopyableCode code="buildEnvVariables" /> | `object` | Environment variables available to the build environment.Only returned in GET requests if view=FULL is set. |
| <CopyableCode code="createTime" /> | `string` | Time that this version was created.@OutputOnly |
| <CopyableCode code="createdBy" /> | `string` | Email address of the user who created this version.@OutputOnly |
| <CopyableCode code="defaultExpiration" /> | `string` | Duration that static files should be cached by web proxies and browsers. Only applicable if the corresponding StaticFilesHandler (https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#StaticFilesHandler) does not specify its own expiration time.Only returned in GET requests if view=FULL is set. |
| <CopyableCode code="deployment" /> | `object` | Code and application artifacts used to deploy a version to App Engine. |
| <CopyableCode code="diskUsageBytes" /> | `string` | Total size in bytes of all the files that are included in this version and currently hosted on the App Engine disk.@OutputOnly |
| <CopyableCode code="endpointsApiService" /> | `object` | Google Cloud Endpoints (https://cloud.google.com/endpoints) configuration. The Endpoints API Service provides tooling for serving Open API and gRPC endpoints via an NGINX proxy. Only valid for App Engine Flexible environment deployments.The fields here refer to the name and configuration ID of a "service" resource in the Service Management API (https://cloud.google.com/service-management/overview). |
| <CopyableCode code="entrypoint" /> | `object` | The entrypoint for the application. |
| <CopyableCode code="env" /> | `string` | App Engine execution environment for this version.Defaults to standard. |
| <CopyableCode code="envVariables" /> | `object` | Environment variables available to the application.Only returned in GET requests if view=FULL is set. |
| <CopyableCode code="errorHandlers" /> | `array` | Custom static error pages. Limited to 10KB per page.Only returned in GET requests if view=FULL is set. |
| <CopyableCode code="flexibleRuntimeSettings" /> | `object` | Runtime settings for the App Engine flexible environment. |
| <CopyableCode code="generatedCustomerMetadata" /> | `object` | Additional Google Generated Customer Metadata, this field won't be provided by default and can be requested by setting the IncludeExtraData field in GetVersionRequest |
| <CopyableCode code="handlers" /> | `array` | An ordered list of URL-matching patterns that should be applied to incoming requests. The first matching URL handles the request and other request handlers are not attempted.Only returned in GET requests if view=FULL is set. |
| <CopyableCode code="healthCheck" /> | `object` | Health checking configuration for VM instances. Unhealthy instances are killed and replaced with new instances. Only applicable for instances in App Engine flexible environment. |
| <CopyableCode code="inboundServices" /> | `array` | Before an application can receive email or XMPP messages, the application must be configured to enable the service. |
| <CopyableCode code="instanceClass" /> | `string` | Instance class that is used to run this version. Valid values are: AutomaticScaling: F1, F2, F4, F4_1G ManualScaling or BasicScaling: B1, B2, B4, B8, B4_1GDefaults to F1 for AutomaticScaling and B1 for ManualScaling or BasicScaling. |
| <CopyableCode code="libraries" /> | `array` | Configuration for third-party Python runtime libraries that are required by the application.Only returned in GET requests if view=FULL is set. |
| <CopyableCode code="livenessCheck" /> | `object` | Health checking configuration for VM instances. Unhealthy instances are killed and replaced with new instances. |
| <CopyableCode code="manualScaling" /> | `object` | A service with manual scaling runs continuously, allowing you to perform complex initialization and rely on the state of its memory over time. |
| <CopyableCode code="network" /> | `object` | Extra network settings. Only applicable in the App Engine flexible environment. |
| <CopyableCode code="nobuildFilesRegex" /> | `string` | Files that match this pattern will not be built into this version. Only applicable for Go runtimes.Only returned in GET requests if view=FULL is set. |
| <CopyableCode code="readinessCheck" /> | `object` | Readiness checking configuration for VM instances. Unhealthy instances are removed from traffic rotation. |
| <CopyableCode code="resources" /> | `object` | Machine resources for a version. |
| <CopyableCode code="runtime" /> | `string` | Desired runtime. Example: python27. |
| <CopyableCode code="runtimeApiVersion" /> | `string` | The version of the API in the given runtime environment. Please see the app.yaml reference for valid values at https://cloud.google.com/appengine/docs/standard//config/appref |
| <CopyableCode code="runtimeChannel" /> | `string` | The channel of the runtime to use. Only available for some runtimes. Defaults to the default channel. |
| <CopyableCode code="runtimeMainExecutablePath" /> | `string` | The path or name of the app's main executable. |
| <CopyableCode code="serviceAccount" /> | `string` | The identity that the deployed version will run as. Admin API will use the App Engine Appspot service account as default if this field is neither provided in app.yaml file nor through CLI flag. |
| <CopyableCode code="servingStatus" /> | `string` | Current serving status of this version. Only the versions with a SERVING status create instances and can be billed.SERVING_STATUS_UNSPECIFIED is an invalid value. Defaults to SERVING. |
| <CopyableCode code="threadsafe" /> | `boolean` | Whether multiple requests can be dispatched to this version at once. |
| <CopyableCode code="versionUrl" /> | `string` | Serving URL for this version. Example: "https://myversion-dot-myservice-dot-myapp.appspot.com"@OutputOnly |
| <CopyableCode code="vm" /> | `boolean` | Whether to deploy this version in a container on a virtual machine. |
| <CopyableCode code="vpcAccessConnector" /> | `object` | VPC access connector specification. |
| <CopyableCode code="zones" /> | `array` | The Google Compute Engine zones that are supported by this version in the App Engine flexible environment. Deprecated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="appsId, servicesId, versionsId" /> | Gets the specified Version resource. By default, only a BASIC_VIEW will be returned. Specify the FULL_VIEW parameter to get the full resource. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="appsId, servicesId" /> | Lists the versions of a service. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="appsId, servicesId" /> | Deploys code and resource files to a new version. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="appsId, servicesId, versionsId" /> | Deletes an existing Version resource. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="appsId, servicesId, versionsId" /> | Updates the specified Version resource. You can specify the following fields depending on the App Engine environment and type of scaling that the version resource uses:Standard environment instance_class (https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#Version.FIELDS.instance_class)automatic scaling in the standard environment: automatic_scaling.min_idle_instances (https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#Version.FIELDS.automatic_scaling) automatic_scaling.max_idle_instances (https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#Version.FIELDS.automatic_scaling) automaticScaling.standard_scheduler_settings.max_instances (https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#StandardSchedulerSettings) automaticScaling.standard_scheduler_settings.min_instances (https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#StandardSchedulerSettings) automaticScaling.standard_scheduler_settings.target_cpu_utilization (https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#StandardSchedulerSettings) automaticScaling.standard_scheduler_settings.target_throughput_utilization (https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#StandardSchedulerSettings)basic scaling or manual scaling in the standard environment: serving_status (https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#Version.FIELDS.serving_status) manual_scaling.instances (https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#manualscaling)Flexible environment serving_status (https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#Version.FIELDS.serving_status)automatic scaling in the flexible environment: automatic_scaling.min_total_instances (https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#Version.FIELDS.automatic_scaling) automatic_scaling.max_total_instances (https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#Version.FIELDS.automatic_scaling) automatic_scaling.cool_down_period_sec (https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#Version.FIELDS.automatic_scaling) automatic_scaling.cpu_utilization.target_utilization (https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#Version.FIELDS.automatic_scaling)manual scaling in the flexible environment: manual_scaling.instances (https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#manualscaling) |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="appsId, servicesId" /> | Lists the versions of a service. |
