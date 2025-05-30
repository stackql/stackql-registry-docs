---
title: configs
hide_title: false
hide_table_of_contents: false
keywords:
  - configs
  - servicemanagement
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

Creates, updates, deletes, gets or lists a <code>configs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>configs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.servicemanagement.configs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | A unique ID for a specific instance of this message, typically assigned by the client for tracking purpose. Must be no longer than 63 characters and only lower case letters, digits, '.', '_' and '-' are allowed. If empty, the server may choose to generate one instead. |
| <CopyableCode code="name" /> | `string` | The service name, which is a DNS-like logical identifier for the service, such as `calendar.googleapis.com`. The service name typically goes through DNS verification to make sure the owner of the service also owns the DNS name. |
| <CopyableCode code="apis" /> | `array` | A list of API interfaces exported by this service. Only the `name` field of the google.protobuf.Api needs to be provided by the configuration author, as the remaining fields will be derived from the IDL during the normalization process. It is an error to specify an API interface here which cannot be resolved against the associated IDL files. |
| <CopyableCode code="authentication" /> | `object` | `Authentication` defines the authentication configuration for API methods provided by an API service. Example: name: calendar.googleapis.com authentication: providers: - id: google_calendar_auth jwks_uri: https://www.googleapis.com/oauth2/v1/certs issuer: https://securetoken.google.com rules: - selector: "*" requirements: provider_id: google_calendar_auth - selector: google.calendar.Delegate oauth: canonical_scopes: https://www.googleapis.com/auth/calendar.read |
| <CopyableCode code="backend" /> | `object` | `Backend` defines the backend configuration for a service. |
| <CopyableCode code="billing" /> | `object` | Billing related configuration of the service. The following example shows how to configure monitored resources and metrics for billing, `consumer_destinations` is the only supported destination and the monitored resources need at least one label key `cloud.googleapis.com/location` to indicate the location of the billing usage, using different monitored resources between monitoring and billing is recommended so they can be evolved independently: monitored_resources: - type: library.googleapis.com/billing_branch labels: - key: cloud.googleapis.com/location description: | Predefined label to support billing location restriction. - key: city description: | Custom label to define the city where the library branch is located in. - key: name description: Custom label to define the name of the library branch. metrics: - name: library.googleapis.com/book/borrowed_count metric_kind: DELTA value_type: INT64 unit: "1" billing: consumer_destinations: - monitored_resource: library.googleapis.com/billing_branch metrics: - library.googleapis.com/book/borrowed_count |
| <CopyableCode code="configVersion" /> | `integer` | Obsolete. Do not use. This field has no semantic meaning. The service config compiler always sets this field to `3`. |
| <CopyableCode code="context" /> | `object` | `Context` defines which contexts an API requests. Example: context: rules: - selector: "*" requested: - google.rpc.context.ProjectContext - google.rpc.context.OriginContext The above specifies that all methods in the API request `google.rpc.context.ProjectContext` and `google.rpc.context.OriginContext`. Available context types are defined in package `google.rpc.context`. This also provides mechanism to allowlist any protobuf message extension that can be sent in grpc metadata using “x-goog-ext--bin” and “x-goog-ext--jspb” format. For example, list any service specific protobuf types that can appear in grpc metadata as follows in your yaml file: Example: context: rules: - selector: "google.example.library.v1.LibraryService.CreateBook" allowed_request_extensions: - google.foo.v1.NewExtension allowed_response_extensions: - google.foo.v1.NewExtension You can also specify extension ID instead of fully qualified extension name here. |
| <CopyableCode code="control" /> | `object` | Selects and configures the service controller used by the service. Example: control: environment: servicecontrol.googleapis.com |
| <CopyableCode code="customError" /> | `object` | Customize service error responses. For example, list any service specific protobuf types that can appear in error detail lists of error responses. Example: custom_error: types: - google.foo.v1.CustomError - google.foo.v1.AnotherError |
| <CopyableCode code="documentation" /> | `object` | `Documentation` provides the information for describing a service. Example: documentation: summary: > The Google Calendar API gives access to most calendar features. pages: - name: Overview content: (== include google/foo/overview.md ==) - name: Tutorial content: (== include google/foo/tutorial.md ==) subpages: - name: Java content: (== include google/foo/tutorial_java.md ==) rules: - selector: google.calendar.Calendar.Get description: > ... - selector: google.calendar.Calendar.Put description: > ... Documentation is provided in markdown syntax. In addition to standard markdown features, definition lists, tables and fenced code blocks are supported. Section headers can be provided and are interpreted relative to the section nesting of the context where a documentation fragment is embedded. Documentation from the IDL is merged with documentation defined via the config at normalization time, where documentation provided by config rules overrides IDL provided. A number of constructs specific to the API platform are supported in documentation text. In order to reference a proto element, the following notation can be used: [fully.qualified.proto.name][] To override the display text used for the link, this can be used: [display text][fully.qualified.proto.name] Text can be excluded from doc using the following notation: (-- internal comment --) A few directives are available in documentation. Note that directives must appear on a single line to be properly identified. The `include` directive includes a markdown file from an external source: (== include path/to/file ==) The `resource_for` directive marks a message to be the resource of a collection in REST view. If it is not specified, tools attempt to infer the resource from the operations in a collection: (== resource_for v1.shelves.books ==) The directive `suppress_warning` does not directly affect documentation and is documented together with service config validation. |
| <CopyableCode code="endpoints" /> | `array` | Configuration for network endpoints. If this is empty, then an endpoint with the same name as the service is automatically generated to service all defined APIs. |
| <CopyableCode code="enums" /> | `array` | A list of all enum types included in this API service. Enums referenced directly or indirectly by the `apis` are automatically included. Enums which are not referenced but shall be included should be listed here by name by the configuration author. Example: enums: - name: google.someapi.v1.SomeEnum |
| <CopyableCode code="http" /> | `object` | Defines the HTTP configuration for an API service. It contains a list of HttpRule, each specifying the mapping of an RPC method to one or more HTTP REST API methods. |
| <CopyableCode code="logging" /> | `object` | Logging configuration of the service. The following example shows how to configure logs to be sent to the producer and consumer projects. In the example, the `activity_history` log is sent to both the producer and consumer projects, whereas the `purchase_history` log is only sent to the producer project. monitored_resources: - type: library.googleapis.com/branch labels: - key: /city description: The city where the library branch is located in. - key: /name description: The name of the branch. logs: - name: activity_history labels: - key: /customer_id - name: purchase_history logging: producer_destinations: - monitored_resource: library.googleapis.com/branch logs: - activity_history - purchase_history consumer_destinations: - monitored_resource: library.googleapis.com/branch logs: - activity_history |
| <CopyableCode code="logs" /> | `array` | Defines the logs used by this service. |
| <CopyableCode code="metrics" /> | `array` | Defines the metrics used by this service. |
| <CopyableCode code="monitoredResources" /> | `array` | Defines the monitored resources used by this service. This is required by the Service.monitoring and Service.logging configurations. |
| <CopyableCode code="monitoring" /> | `object` | Monitoring configuration of the service. The example below shows how to configure monitored resources and metrics for monitoring. In the example, a monitored resource and two metrics are defined. The `library.googleapis.com/book/returned_count` metric is sent to both producer and consumer projects, whereas the `library.googleapis.com/book/num_overdue` metric is only sent to the consumer project. monitored_resources: - type: library.googleapis.com/Branch display_name: "Library Branch" description: "A branch of a library." launch_stage: GA labels: - key: resource_container description: "The Cloud container (ie. project id) for the Branch." - key: location description: "The location of the library branch." - key: branch_id description: "The id of the branch." metrics: - name: library.googleapis.com/book/returned_count display_name: "Books Returned" description: "The count of books that have been returned." launch_stage: GA metric_kind: DELTA value_type: INT64 unit: "1" labels: - key: customer_id description: "The id of the customer." - name: library.googleapis.com/book/num_overdue display_name: "Books Overdue" description: "The current number of overdue books." launch_stage: GA metric_kind: GAUGE value_type: INT64 unit: "1" labels: - key: customer_id description: "The id of the customer." monitoring: producer_destinations: - monitored_resource: library.googleapis.com/Branch metrics: - library.googleapis.com/book/returned_count consumer_destinations: - monitored_resource: library.googleapis.com/Branch metrics: - library.googleapis.com/book/returned_count - library.googleapis.com/book/num_overdue |
| <CopyableCode code="producerProjectId" /> | `string` | The Google project that owns this service. |
| <CopyableCode code="publishing" /> | `object` | This message configures the settings for publishing [Google Cloud Client libraries](https://cloud.google.com/apis/docs/cloud-client-libraries) generated from the service config. |
| <CopyableCode code="quota" /> | `object` | Quota configuration helps to achieve fairness and budgeting in service usage. The metric based quota configuration works this way: - The service configuration defines a set of metrics. - For API calls, the quota.metric_rules maps methods to metrics with corresponding costs. - The quota.limits defines limits on the metrics, which will be used for quota checks at runtime. An example quota configuration in yaml format: quota: limits: - name: apiWriteQpsPerProject metric: library.googleapis.com/write_calls unit: "1/min/{project}" # rate limit for consumer projects values: STANDARD: 10000 (The metric rules bind all methods to the read_calls metric, except for the UpdateBook and DeleteBook methods. These two methods are mapped to the write_calls metric, with the UpdateBook method consuming at twice rate as the DeleteBook method.) metric_rules: - selector: "*" metric_costs: library.googleapis.com/read_calls: 1 - selector: google.example.library.v1.LibraryService.UpdateBook metric_costs: library.googleapis.com/write_calls: 2 - selector: google.example.library.v1.LibraryService.DeleteBook metric_costs: library.googleapis.com/write_calls: 1 Corresponding Metric definition: metrics: - name: library.googleapis.com/read_calls display_name: Read requests metric_kind: DELTA value_type: INT64 - name: library.googleapis.com/write_calls display_name: Write requests metric_kind: DELTA value_type: INT64  |
| <CopyableCode code="sourceInfo" /> | `object` | Source information used to create a Service Config |
| <CopyableCode code="systemParameters" /> | `object` | ### System parameter configuration A system parameter is a special kind of parameter defined by the API system, not by an individual API. It is typically mapped to an HTTP header and/or a URL query parameter. This configuration specifies which methods change the names of the system parameters. |
| <CopyableCode code="systemTypes" /> | `array` | A list of all proto message types included in this API service. It serves similar purpose as [google.api.Service.types], except that these types are not needed by user-defined APIs. Therefore, they will not show up in the generated discovery doc. This field should only be used to define system APIs in ESF. |
| <CopyableCode code="title" /> | `string` | The product title for this service, it is the name displayed in Google Cloud Console. |
| <CopyableCode code="types" /> | `array` | A list of all proto message types included in this API service. Types referenced directly or indirectly by the `apis` are automatically included. Messages which are not referenced but shall be included, such as types used by the `google.protobuf.Any` type, should be listed here by name by the configuration author. Example: types: - name: google.protobuf.Int32 |
| <CopyableCode code="usage" /> | `object` | Configuration controlling usage of a service. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="configId, serviceName" /> | Gets a service configuration (version) for a managed service. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="serviceName" /> | Lists the history of the service configuration for a managed service, from the newest to the oldest. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="serviceName" /> | Creates a new service configuration (version) for a managed service. This method only stores the service configuration. To roll out the service configuration to backend systems please call CreateServiceRollout. Only the 100 most recent service configurations and ones referenced by existing rollouts are kept for each service. The rest will be deleted eventually. |
| <CopyableCode code="submit" /> | `EXEC` | <CopyableCode code="serviceName" /> | Creates a new service configuration (version) for a managed service based on user-supplied configuration source files (for example: OpenAPI Specification). This method stores the source configurations as well as the generated service configuration. To rollout the service configuration to other services, please call CreateServiceRollout. Only the 100 most recent configuration sources and ones referenced by existing service configurtions are kept for each service. The rest will be deleted eventually. Operation |

## `SELECT` examples

Lists the history of the service configuration for a managed service, from the newest to the oldest.

```sql
SELECT
id,
name,
apis,
authentication,
backend,
billing,
configVersion,
context,
control,
customError,
documentation,
endpoints,
enums,
http,
logging,
logs,
metrics,
monitoredResources,
monitoring,
producerProjectId,
publishing,
quota,
sourceInfo,
systemParameters,
systemTypes,
title,
types,
usage
FROM google.servicemanagement.configs
WHERE serviceName = '{{ serviceName }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>configs</code> resource.

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
INSERT INTO google.servicemanagement.configs (
serviceName,
name,
title,
producerProjectId,
apis,
types,
enums,
documentation,
backend,
http,
quota,
authentication,
context,
usage,
customError,
endpoints,
control,
logs,
metrics,
monitoredResources,
billing,
logging,
monitoring,
systemParameters,
sourceInfo,
publishing,
systemTypes,
configVersion
)
SELECT 
'{{ serviceName }}',
'{{ name }}',
'{{ title }}',
'{{ producerProjectId }}',
'{{ apis }}',
'{{ types }}',
'{{ enums }}',
'{{ documentation }}',
'{{ backend }}',
'{{ http }}',
'{{ quota }}',
'{{ authentication }}',
'{{ context }}',
'{{ usage }}',
'{{ customError }}',
'{{ endpoints }}',
'{{ control }}',
'{{ logs }}',
'{{ metrics }}',
'{{ monitoredResources }}',
'{{ billing }}',
'{{ logging }}',
'{{ monitoring }}',
'{{ systemParameters }}',
'{{ sourceInfo }}',
'{{ publishing }}',
'{{ systemTypes }}',
'{{ configVersion }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: string
    - name: title
      value: string
    - name: producerProjectId
      value: string
    - name: id
      value: string
    - name: apis
      value:
        - - name: name
            value: string
          - name: methods
            value:
              - - name: name
                  value: string
                - name: requestTypeUrl
                  value: string
                - name: requestStreaming
                  value: boolean
                - name: responseTypeUrl
                  value: string
                - name: responseStreaming
                  value: boolean
                - name: options
                  value:
                    - - name: name
                        value: string
                      - name: value
                        value: object
                - name: syntax
                  value: string
          - name: options
            value:
              - - name: name
                  value: string
                - name: value
                  value: object
          - name: version
            value: string
          - name: sourceContext
            value:
              - name: fileName
                value: string
          - name: mixins
            value:
              - - name: name
                  value: string
                - name: root
                  value: string
          - name: syntax
            value: string
    - name: types
      value:
        - - name: name
            value: string
          - name: fields
            value:
              - - name: kind
                  value: string
                - name: cardinality
                  value: string
                - name: number
                  value: integer
                - name: name
                  value: string
                - name: typeUrl
                  value: string
                - name: oneofIndex
                  value: integer
                - name: packed
                  value: boolean
                - name: options
                  value:
                    - - name: name
                        value: string
                      - name: value
                        value: object
                - name: jsonName
                  value: string
                - name: defaultValue
                  value: string
          - name: oneofs
            value:
              - string
          - name: options
            value:
              - - name: name
                  value: string
                - name: value
                  value: object
          - name: syntax
            value: string
          - name: edition
            value: string
    - name: enums
      value:
        - - name: name
            value: string
          - name: enumvalue
            value:
              - - name: name
                  value: string
                - name: number
                  value: integer
                - name: options
                  value:
                    - - name: name
                        value: string
                      - name: value
                        value: object
          - name: options
            value:
              - - name: name
                  value: string
                - name: value
                  value: object
          - name: syntax
            value: string
          - name: edition
            value: string
    - name: documentation
      value:
        - name: summary
          value: string
        - name: pages
          value:
            - - name: name
                value: string
              - name: content
                value: string
              - name: subpages
                value:
                  - - name: name
                      value: string
                    - name: content
                      value: string
                    - name: subpages
                      value:
                        - - name: name
                            value: string
                          - name: content
                            value: string
                          - name: subpages
                            value:
                              - - name: name
                                  value: string
                                - name: content
                                  value: string
                                - name: subpages
                                  value:
                                    - - name: name
                                        value: string
                                      - name: content
                                        value: string
                                      - name: subpages
                                        value:
                                          - - name: name
                                              value: string
                                            - name: content
                                              value: string
                                            - name: subpages
                                              value:
                                                - - name: name
                                                    value: string
                                                  - name: content
                                                    value: string
                                                  - name: subpages
                                                    value:
                                                      - - name: name
                                                          value: string
                                                        - name: content
                                                          value: string
                                                        - name: subpages
                                                          value:
                                                            - - name: name
                                                                value: string
                                                              - name: content
                                                                value: string
                                                              - name: subpages
                                                                value:
                                                                  - []
        - name: rules
          value:
            - - name: selector
                value: string
              - name: description
                value: string
              - name: deprecationDescription
                value: string
              - name: disableReplacementWords
                value: string
        - name: documentationRootUrl
          value: string
        - name: serviceRootUrl
          value: string
        - name: overview
          value: string
        - name: sectionOverrides
          value:
            - - name: name
                value: string
              - name: content
                value: string
              - name: subpages
                value:
                  - - name: name
                      value: string
                    - name: content
                      value: string
                    - name: subpages
                      value:
                        - - name: name
                            value: string
                          - name: content
                            value: string
                          - name: subpages
                            value:
                              - - name: name
                                  value: string
                                - name: content
                                  value: string
                                - name: subpages
                                  value:
                                    - - name: name
                                        value: string
                                      - name: content
                                        value: string
                                      - name: subpages
                                        value:
                                          - - name: name
                                              value: string
                                            - name: content
                                              value: string
                                            - name: subpages
                                              value:
                                                - - name: name
                                                    value: string
                                                  - name: content
                                                    value: string
                                                  - name: subpages
                                                    value:
                                                      - - name: name
                                                          value: string
                                                        - name: content
                                                          value: string
                                                        - name: subpages
                                                          value:
                                                            - - name: name
                                                                value: string
                                                              - name: content
                                                                value: string
                                                              - name: subpages
                                                                value:
                                                                  - []
    - name: backend
      value:
        - name: rules
          value:
            - - name: selector
                value: string
              - name: address
                value: string
              - name: deadline
                value: number
              - name: minDeadline
                value: number
              - name: operationDeadline
                value: number
              - name: pathTranslation
                value: string
              - name: jwtAudience
                value: string
              - name: disableAuth
                value: boolean
              - name: protocol
                value: string
              - name: overridesByRequestProtocol
                value: object
    - name: http
      value:
        - name: rules
          value:
            - - name: selector
                value: string
              - name: get
                value: string
              - name: put
                value: string
              - name: post
                value: string
              - name: delete
                value: string
              - name: patch
                value: string
              - name: custom
                value:
                  - name: kind
                    value: string
                  - name: path
                    value: string
              - name: body
                value: string
              - name: responseBody
                value: string
              - name: additionalBindings
                value:
                  - - name: selector
                      value: string
                    - name: get
                      value: string
                    - name: put
                      value: string
                    - name: post
                      value: string
                    - name: delete
                      value: string
                    - name: patch
                      value: string
                    - name: body
                      value: string
                    - name: responseBody
                      value: string
                    - name: additionalBindings
                      value:
                        - - name: selector
                            value: string
                          - name: get
                            value: string
                          - name: put
                            value: string
                          - name: post
                            value: string
                          - name: delete
                            value: string
                          - name: patch
                            value: string
                          - name: body
                            value: string
                          - name: responseBody
                            value: string
                          - name: additionalBindings
                            value:
                              - - name: selector
                                  value: string
                                - name: get
                                  value: string
                                - name: put
                                  value: string
                                - name: post
                                  value: string
                                - name: delete
                                  value: string
                                - name: patch
                                  value: string
                                - name: body
                                  value: string
                                - name: responseBody
                                  value: string
                                - name: additionalBindings
                                  value:
                                    - - name: selector
                                        value: string
                                      - name: get
                                        value: string
                                      - name: put
                                        value: string
                                      - name: post
                                        value: string
                                      - name: delete
                                        value: string
                                      - name: patch
                                        value: string
                                      - name: body
                                        value: string
                                      - name: responseBody
                                        value: string
                                      - name: additionalBindings
                                        value:
                                          - - name: selector
                                              value: string
                                            - name: get
                                              value: string
                                            - name: put
                                              value: string
                                            - name: post
                                              value: string
                                            - name: delete
                                              value: string
                                            - name: patch
                                              value: string
                                            - name: body
                                              value: string
                                            - name: responseBody
                                              value: string
                                            - name: additionalBindings
                                              value:
                                                - - name: selector
                                                    value: string
                                                  - name: get
                                                    value: string
                                                  - name: put
                                                    value: string
                                                  - name: post
                                                    value: string
                                                  - name: delete
                                                    value: string
                                                  - name: patch
                                                    value: string
                                                  - name: body
                                                    value: string
                                                  - name: responseBody
                                                    value: string
                                                  - name: additionalBindings
                                                    value:
                                                      - - name: selector
                                                          value: string
                                                        - name: get
                                                          value: string
                                                        - name: put
                                                          value: string
                                                        - name: post
                                                          value: string
                                                        - name: delete
                                                          value: string
                                                        - name: patch
                                                          value: string
                                                        - name: body
                                                          value: string
                                                        - name: responseBody
                                                          value: string
                                                        - name: additionalBindings
                                                          value:
                                                            - - name: selector
                                                                value: string
                                                              - name: get
                                                                value: string
                                                              - name: put
                                                                value: string
                                                              - name: post
                                                                value: string
                                                              - name: delete
                                                                value: string
                                                              - name: patch
                                                                value: string
                                                              - name: body
                                                                value: string
                                                              - name: responseBody
                                                                value: string
                                                              - name: additionalBindings
                                                                value:
                                                                  - []
        - name: fullyDecodeReservedExpansion
          value: boolean
    - name: quota
      value:
        - name: limits
          value:
            - - name: name
                value: string
              - name: description
                value: string
              - name: defaultLimit
                value: string
              - name: maxLimit
                value: string
              - name: freeTier
                value: string
              - name: duration
                value: string
              - name: metric
                value: string
              - name: unit
                value: string
              - name: values
                value: object
              - name: displayName
                value: string
        - name: metricRules
          value:
            - - name: selector
                value: string
              - name: metricCosts
                value: object
    - name: authentication
      value:
        - name: rules
          value:
            - - name: selector
                value: string
              - name: oauth
                value:
                  - name: canonicalScopes
                    value: string
              - name: allowWithoutCredential
                value: boolean
              - name: requirements
                value:
                  - - name: providerId
                      value: string
                    - name: audiences
                      value: string
        - name: providers
          value:
            - - name: id
                value: string
              - name: issuer
                value: string
              - name: jwksUri
                value: string
              - name: audiences
                value: string
              - name: authorizationUrl
                value: string
              - name: jwtLocations
                value:
                  - - name: header
                      value: string
                    - name: query
                      value: string
                    - name: cookie
                      value: string
                    - name: valuePrefix
                      value: string
    - name: context
      value:
        - name: rules
          value:
            - - name: selector
                value: string
              - name: requested
                value:
                  - string
              - name: provided
                value:
                  - string
              - name: allowedRequestExtensions
                value:
                  - string
              - name: allowedResponseExtensions
                value:
                  - string
    - name: usage
      value:
        - name: requirements
          value:
            - string
        - name: rules
          value:
            - - name: selector
                value: string
              - name: allowUnregisteredCalls
                value: boolean
              - name: skipServiceControl
                value: boolean
        - name: producerNotificationChannel
          value: string
    - name: customError
      value:
        - name: rules
          value:
            - - name: selector
                value: string
              - name: isErrorType
                value: boolean
        - name: types
          value:
            - string
    - name: endpoints
      value:
        - - name: name
            value: string
          - name: aliases
            value:
              - string
          - name: target
            value: string
          - name: allowCors
            value: boolean
    - name: control
      value:
        - name: environment
          value: string
        - name: methodPolicies
          value:
            - - name: selector
                value: string
              - name: requestPolicies
                value:
                  - - name: selector
                      value: string
                    - name: resourcePermission
                      value: string
                    - name: resourceType
                      value: string
    - name: logs
      value:
        - - name: name
            value: string
          - name: labels
            value:
              - - name: key
                  value: string
                - name: valueType
                  value: string
                - name: description
                  value: string
          - name: description
            value: string
          - name: displayName
            value: string
    - name: metrics
      value:
        - - name: name
            value: string
          - name: type
            value: string
          - name: labels
            value:
              - - name: key
                  value: string
                - name: valueType
                  value: string
                - name: description
                  value: string
          - name: metricKind
            value: string
          - name: valueType
            value: string
          - name: unit
            value: string
          - name: description
            value: string
          - name: displayName
            value: string
          - name: metadata
            value:
              - name: launchStage
                value: string
              - name: samplePeriod
                value: string
              - name: ingestDelay
                value: string
              - name: timeSeriesResourceHierarchyLevel
                value:
                  - string
          - name: launchStage
            value: string
          - name: monitoredResourceTypes
            value:
              - string
    - name: monitoredResources
      value:
        - - name: name
            value: string
          - name: type
            value: string
          - name: displayName
            value: string
          - name: description
            value: string
          - name: labels
            value:
              - - name: key
                  value: string
                - name: valueType
                  value: string
                - name: description
                  value: string
          - name: launchStage
            value: string
    - name: billing
      value:
        - name: consumerDestinations
          value:
            - - name: monitoredResource
                value: string
              - name: metrics
                value:
                  - string
    - name: logging
      value:
        - name: producerDestinations
          value:
            - - name: monitoredResource
                value: string
              - name: logs
                value:
                  - string
        - name: consumerDestinations
          value:
            - - name: monitoredResource
                value: string
              - name: logs
                value:
                  - string
    - name: monitoring
      value:
        - name: producerDestinations
          value:
            - - name: monitoredResource
                value: string
              - name: metrics
                value:
                  - string
        - name: consumerDestinations
          value:
            - - name: monitoredResource
                value: string
              - name: metrics
                value:
                  - string
    - name: systemParameters
      value:
        - name: rules
          value:
            - - name: selector
                value: string
              - name: parameters
                value:
                  - - name: name
                      value: string
                    - name: httpHeader
                      value: string
                    - name: urlQueryParameter
                      value: string
    - name: sourceInfo
      value:
        - name: sourceFiles
          value:
            - object
    - name: publishing
      value:
        - name: methodSettings
          value:
            - - name: selector
                value: string
              - name: longRunning
                value:
                  - name: initialPollDelay
                    value: string
                  - name: pollDelayMultiplier
                    value: number
                  - name: maxPollDelay
                    value: string
                  - name: totalPollTimeout
                    value: string
              - name: autoPopulatedFields
                value:
                  - string
        - name: newIssueUri
          value: string
        - name: documentationUri
          value: string
        - name: apiShortName
          value: string
        - name: githubLabel
          value: string
        - name: codeownerGithubTeams
          value:
            - string
        - name: docTagPrefix
          value: string
        - name: organization
          value: string
        - name: librarySettings
          value:
            - - name: version
                value: string
              - name: launchStage
                value: string
              - name: restNumericEnums
                value: boolean
              - name: javaSettings
                value:
                  - name: libraryPackage
                    value: string
                  - name: serviceClassNames
                    value: object
                  - name: common
                    value:
                      - name: referenceDocsUri
                        value: string
                      - name: destinations
                        value:
                          - string
              - name: cppSettings
                value: []
              - name: phpSettings
                value: []
              - name: pythonSettings
                value:
                  - name: experimentalFeatures
                    value:
                      - name: restAsyncIoEnabled
                        value: boolean
              - name: nodeSettings
                value: []
              - name: dotnetSettings
                value:
                  - name: renamedServices
                    value: object
                  - name: renamedResources
                    value: object
                  - name: ignoredResources
                    value:
                      - string
                  - name: forcedNamespaceAliases
                    value:
                      - string
                  - name: handwrittenSignatures
                    value:
                      - string
              - name: rubySettings
                value: []
              - name: goSettings
                value: []
        - name: protoReferenceDocumentationUri
          value: string
        - name: restReferenceDocumentationUri
          value: string
    - name: systemTypes
      value:
        - - name: name
            value: string
          - name: fields
            value:
              - - name: kind
                  value: string
                - name: cardinality
                  value: string
                - name: number
                  value: integer
                - name: name
                  value: string
                - name: typeUrl
                  value: string
                - name: oneofIndex
                  value: integer
                - name: packed
                  value: boolean
                - name: options
                  value:
                    - - name: name
                        value: string
                      - name: value
                        value: object
                - name: jsonName
                  value: string
                - name: defaultValue
                  value: string
          - name: oneofs
            value:
              - string
          - name: options
            value:
              - - name: name
                  value: string
                - name: value
                  value: object
          - name: syntax
            value: string
          - name: edition
            value: string
    - name: configVersion
      value: integer

```
</TabItem>
</Tabs>
