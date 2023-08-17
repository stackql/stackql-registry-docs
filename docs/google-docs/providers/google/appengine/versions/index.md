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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.appengine.versions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Relative name of the version within the service. Example: v1. Version names can contain only lowercase letters, numbers, or hyphens. Reserved names: "default", "latest", and any name with the prefix "ah-". |
| `name` | `string` | Full path to the Version resource in the API. Example: apps/myapp/services/default/versions/v1.@OutputOnly |
| `createdBy` | `string` | Email address of the user who created this version.@OutputOnly |
| `manualScaling` | `object` | A service with manual scaling runs continuously, allowing you to perform complex initialization and rely on the state of its memory over time. |
| `flexibleRuntimeSettings` | `object` | Runtime settings for the App Engine flexible environment. |
| `inboundServices` | `array` | Before an application can receive email or XMPP messages, the application must be configured to enable the service. |
| `runtimeChannel` | `string` | The channel of the runtime to use. Only available for some runtimes. Defaults to the default channel. |
| `healthCheck` | `object` | Health checking configuration for VM instances. Unhealthy instances are killed and replaced with new instances. Only applicable for instances in App Engine flexible environment. |
| `betaSettings` | `object` | Metadata settings that are supplied to this version to enable beta runtime features. |
| `threadsafe` | `boolean` | Whether multiple requests can be dispatched to this version at once. |
| `servingStatus` | `string` | Current serving status of this version. Only the versions with a SERVING status create instances and can be billed.SERVING_STATUS_UNSPECIFIED is an invalid value. Defaults to SERVING. |
| `instanceClass` | `string` | Instance class that is used to run this version. Valid values are: AutomaticScaling: F1, F2, F4, F4_1G ManualScaling or BasicScaling: B1, B2, B4, B8, B4_1GDefaults to F1 for AutomaticScaling and B1 for ManualScaling or BasicScaling. |
| `versionUrl` | `string` | Serving URL for this version. Example: "https://myversion-dot-myservice-dot-myapp.appspot.com"@OutputOnly |
| `handlers` | `array` | An ordered list of URL-matching patterns that should be applied to incoming requests. The first matching URL handles the request and other request handlers are not attempted.Only returned in GET requests if view=FULL is set. |
| `zones` | `array` | The Google Compute Engine zones that are supported by this version in the App Engine flexible environment. Deprecated. |
| `network` | `object` | Extra network settings. Only applicable in the App Engine flexible environment. |
| `basicScaling` | `object` | A service with basic scaling will create an instance when the application receives a request. The instance will be turned down when the app becomes idle. Basic scaling is ideal for work that is intermittent or driven by user activity. |
| `env` | `string` | App Engine execution environment for this version.Defaults to standard. |
| `livenessCheck` | `object` | Health checking configuration for VM instances. Unhealthy instances are killed and replaced with new instances. |
| `runtime` | `string` | Desired runtime. Example: python27. |
| `buildEnvVariables` | `object` | Environment variables available to the build environment.Only returned in GET requests if view=FULL is set. |
| `endpointsApiService` | `object` | Google Cloud Endpoints (https://cloud.google.com/endpoints) configuration. The Endpoints API Service provides tooling for serving Open API and gRPC endpoints via an NGINX proxy. Only valid for App Engine Flexible environment deployments.The fields here refer to the name and configuration ID of a "service" resource in the Service Management API (https://cloud.google.com/service-management/overview). |
| `deployment` | `object` | Code and application artifacts used to deploy a version to App Engine. |
| `appEngineApis` | `boolean` | Allows App Engine second generation runtimes to access the legacy bundled services. |
| `entrypoint` | `object` | The entrypoint for the application. |
| `runtimeMainExecutablePath` | `string` | The path or name of the app's main executable. |
| `defaultExpiration` | `string` | Duration that static files should be cached by web proxies and browsers. Only applicable if the corresponding StaticFilesHandler (https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#StaticFilesHandler) does not specify its own expiration time.Only returned in GET requests if view=FULL is set. |
| `diskUsageBytes` | `string` | Total size in bytes of all the files that are included in this version and currently hosted on the App Engine disk.@OutputOnly |
| `errorHandlers` | `array` | Custom static error pages. Limited to 10KB per page.Only returned in GET requests if view=FULL is set. |
| `resources` | `object` | Machine resources for a version. |
| `vm` | `boolean` | Whether to deploy this version in a container on a virtual machine. |
| `automaticScaling` | `object` | Automatic scaling is based on request rate, response latencies, and other application metrics. |
| `nobuildFilesRegex` | `string` | Files that match this pattern will not be built into this version. Only applicable for Go runtimes.Only returned in GET requests if view=FULL is set. |
| `runtimeApiVersion` | `string` | The version of the API in the given runtime environment. Please see the app.yaml reference for valid values at https://cloud.google.com/appengine/docs/standard//config/appref |
| `readinessCheck` | `object` | Readiness checking configuration for VM instances. Unhealthy instances are removed from traffic rotation. |
| `apiConfig` | `object` | Google Cloud Endpoints (https://cloud.google.com/endpoints) configuration for API handlers. |
| `libraries` | `array` | Configuration for third-party Python runtime libraries that are required by the application.Only returned in GET requests if view=FULL is set. |
| `vpcAccessConnector` | `object` | VPC access connector specification. |
| `envVariables` | `object` | Environment variables available to the application.Only returned in GET requests if view=FULL is set. |
| `serviceAccount` | `string` | The identity that the deployed version will run as. Admin API will use the App Engine Appspot service account as default if this field is neither provided in app.yaml file nor through CLI flag. |
| `createTime` | `string` | Time that this version was created.@OutputOnly |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `appsId, servicesId, versionsId` | Gets the specified Version resource. By default, only a BASIC_VIEW will be returned. Specify the FULL_VIEW parameter to get the full resource. |
| `list` | `SELECT` | `appsId, servicesId` | Lists the versions of a service. |
| `create` | `INSERT` | `appsId, servicesId` | Deploys code and resource files to a new version. |
| `delete` | `DELETE` | `appsId, servicesId, versionsId` | Deletes an existing Version resource. |
| `_list` | `EXEC` | `appsId, servicesId` | Lists the versions of a service. |
| `patch` | `EXEC` | `appsId, servicesId, versionsId` | Updates the specified Version resource. You can specify the following fields depending on the App Engine environment and type of scaling that the version resource uses:Standard environment instance_class (https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#Version.FIELDS.instance_class)automatic scaling in the standard environment: automatic_scaling.min_idle_instances (https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#Version.FIELDS.automatic_scaling) automatic_scaling.max_idle_instances (https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#Version.FIELDS.automatic_scaling) automaticScaling.standard_scheduler_settings.max_instances (https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#StandardSchedulerSettings) automaticScaling.standard_scheduler_settings.min_instances (https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#StandardSchedulerSettings) automaticScaling.standard_scheduler_settings.target_cpu_utilization (https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#StandardSchedulerSettings) automaticScaling.standard_scheduler_settings.target_throughput_utilization (https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#StandardSchedulerSettings)basic scaling or manual scaling in the standard environment: serving_status (https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#Version.FIELDS.serving_status) manual_scaling.instances (https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#manualscaling)Flexible environment serving_status (https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#Version.FIELDS.serving_status)automatic scaling in the flexible environment: automatic_scaling.min_total_instances (https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#Version.FIELDS.automatic_scaling) automatic_scaling.max_total_instances (https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#Version.FIELDS.automatic_scaling) automatic_scaling.cool_down_period_sec (https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#Version.FIELDS.automatic_scaling) automatic_scaling.cpu_utilization.target_utilization (https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#Version.FIELDS.automatic_scaling)manual scaling in the flexible environment: manual_scaling.instances (https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#manualscaling) |
