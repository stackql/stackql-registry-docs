---
title: api_management
hide_title: false
hide_table_of_contents: false
keywords:
  - api_management
  - azure
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---

Azure API Management provides a REST API for performing operations on selected entities, such as users, groups, products, and subscriptions. This reference provides a guide for working with the API Management REST API, and specific reference information for each available operation, grouped by entity.  
    
:::info Service Summary

<div class="row">
<div class="providerDocColumn">
<span>total resources:&nbsp;<b>154</b></span><br />
<span>total selectable resources:&nbsp;<b>147</b></span><br />
<span>total methods:&nbsp;<b>529</b></span><br />
</div>
</div>

:::

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>azure.api_management</code></td></tr>
<tr><td><b>Type</b></td><td>Service</td></tr>
<tr><td><b>Title</b></td><td>Azure API Management</td></tr>
<tr><td><b>Description</b></td><td>Azure API Management provides a REST API for performing operations on selected entities, such as users, groups, products, and subscriptions. This reference provides a guide for working with the API Management REST API, and specific reference information for each available operation, grouped by entity.</td></tr>
<tr><td><b>Id</b></td><td><code>azure:api_management</code></td></tr>
</tbody></table>

## Resources
<div class="row">
<div class="providerDocColumn">
<a href="/providers/azure/api_management/all_policies/">all_policies</a><br />
<a href="/providers/azure/api_management/api/">api</a><br />
<a href="/providers/azure/api_management/api_diagnostic/">api_diagnostic</a><br />
<a href="/providers/azure/api_management/api_gateway/">api_gateway</a><br />
<a href="/providers/azure/api_management/api_gateway_config_connection/">api_gateway_config_connection</a><br />
<a href="/providers/azure/api_management/api_issue/">api_issue</a><br />
<a href="/providers/azure/api_management/api_issue_attachment/">api_issue_attachment</a><br />
<a href="/providers/azure/api_management/api_issue_comment/">api_issue_comment</a><br />
<a href="/providers/azure/api_management/api_operation/">api_operation</a><br />
<a href="/providers/azure/api_management/api_operation_policy/">api_operation_policy</a><br />
<a href="/providers/azure/api_management/api_policy/">api_policy</a><br />
<a href="/providers/azure/api_management/api_product/">api_product</a><br />
<a href="/providers/azure/api_management/api_release/">api_release</a><br />
<a href="/providers/azure/api_management/api_revision/">api_revision</a><br />
<a href="/providers/azure/api_management/api_schema/">api_schema</a><br />
<a href="/providers/azure/api_management/api_tag_description/">api_tag_description</a><br />
<a href="/providers/azure/api_management/api_version_set/">api_version_set</a><br />
<a href="/providers/azure/api_management/api_wiki/">api_wiki</a><br />
<a href="/providers/azure/api_management/api_wikis/">api_wikis</a><br />
<a href="/providers/azure/api_management/authorization/">authorization</a><br />
<a href="/providers/azure/api_management/authorization_access_policy/">authorization_access_policy</a><br />
<a href="/providers/azure/api_management/authorization_login_links/">authorization_login_links</a><br />
<a href="/providers/azure/api_management/authorization_provider/">authorization_provider</a><br />
<a href="/providers/azure/api_management/authorization_server/">authorization_server</a><br />
<a href="/providers/azure/api_management/authorization_server_secrets/">authorization_server_secrets</a><br />
<a href="/providers/azure/api_management/backend/">backend</a><br />
<a href="/providers/azure/api_management/cache/">cache</a><br />
<a href="/providers/azure/api_management/certificate/">certificate</a><br />
<a href="/providers/azure/api_management/content_item/">content_item</a><br />
<a href="/providers/azure/api_management/content_type/">content_type</a><br />
<a href="/providers/azure/api_management/delegation_settings/">delegation_settings</a><br />
<a href="/providers/azure/api_management/delegation_settings_secrets/">delegation_settings_secrets</a><br />
<a href="/providers/azure/api_management/deleted_services/">deleted_services</a><br />
<a href="/providers/azure/api_management/diagnostic/">diagnostic</a><br />
<a href="/providers/azure/api_management/documentation/">documentation</a><br />
<a href="/providers/azure/api_management/email_template/">email_template</a><br />
<a href="/providers/azure/api_management/gateway/">gateway</a><br />
<a href="/providers/azure/api_management/gateway_api/">gateway_api</a><br />
<a href="/providers/azure/api_management/gateway_certificate_authority/">gateway_certificate_authority</a><br />
<a href="/providers/azure/api_management/gateway_debug_credentials/">gateway_debug_credentials</a><br />
<a href="/providers/azure/api_management/gateway_hostname_configuration/">gateway_hostname_configuration</a><br />
<a href="/providers/azure/api_management/gateway_keys/">gateway_keys</a><br />
<a href="/providers/azure/api_management/gateway_skus_available_skus/">gateway_skus_available_skus</a><br />
<a href="/providers/azure/api_management/global_schema/">global_schema</a><br />
<a href="/providers/azure/api_management/graph_ql_api_resolver/">graph_ql_api_resolver</a><br />
<a href="/providers/azure/api_management/graph_ql_api_resolver_policy/">graph_ql_api_resolver_policy</a><br />
<a href="/providers/azure/api_management/group/">group</a><br />
<a href="/providers/azure/api_management/group_user/">group_user</a><br />
<a href="/providers/azure/api_management/identity_provider/">identity_provider</a><br />
<a href="/providers/azure/api_management/identity_provider_secrets/">identity_provider_secrets</a><br />
<a href="/providers/azure/api_management/issue/">issue</a><br />
<a href="/providers/azure/api_management/logger/">logger</a><br />
<a href="/providers/azure/api_management/named_value/">named_value</a><br />
<a href="/providers/azure/api_management/named_value_value/">named_value_value</a><br />
<a href="/providers/azure/api_management/network_status/">network_status</a><br />
<a href="/providers/azure/api_management/notification/">notification</a><br />
<a href="/providers/azure/api_management/notification_recipient_email/">notification_recipient_email</a><br />
<a href="/providers/azure/api_management/notification_recipient_user/">notification_recipient_user</a><br />
<a href="/providers/azure/api_management/open_id_connect_provider/">open_id_connect_provider</a><br />
<a href="/providers/azure/api_management/open_id_connect_provider_secrets/">open_id_connect_provider_secrets</a><br />
<a href="/providers/azure/api_management/operation/">operation</a><br />
<a href="/providers/azure/api_management/operation_status/">operation_status</a><br />
<a href="/providers/azure/api_management/operations/">operations</a><br />
<a href="/providers/azure/api_management/operations_results/">operations_results</a><br />
<a href="/providers/azure/api_management/outbound_network_dependencies_endpoints/">outbound_network_dependencies_endpoints</a><br />
<a href="/providers/azure/api_management/perform_connectivity_check/">perform_connectivity_check</a><br />
<a href="/providers/azure/api_management/policy/">policy</a><br />
<a href="/providers/azure/api_management/policy_description/">policy_description</a><br />
<a href="/providers/azure/api_management/policy_fragment/">policy_fragment</a><br />
<a href="/providers/azure/api_management/policy_fragment_references/">policy_fragment_references</a><br />
<a href="/providers/azure/api_management/policy_restriction/">policy_restriction</a><br />
<a href="/providers/azure/api_management/policy_restriction_validations/">policy_restriction_validations</a><br />
<a href="/providers/azure/api_management/portal_config/">portal_config</a><br />
<a href="/providers/azure/api_management/portal_revision/">portal_revision</a><br />
<a href="/providers/azure/api_management/portal_settings/">portal_settings</a><br />
<a href="/providers/azure/api_management/private_endpoint_connection/">private_endpoint_connection</a><br />
<a href="/providers/azure/api_management/private_endpoint_connection_private_link_resource/">private_endpoint_connection_private_link_resource</a><br />
</div>
<div class="providerDocColumn">
<a href="/providers/azure/api_management/private_endpoint_connection_private_link_resources/">private_endpoint_connection_private_link_resources</a><br />
<a href="/providers/azure/api_management/product/">product</a><br />
<a href="/providers/azure/api_management/product_api/">product_api</a><br />
<a href="/providers/azure/api_management/product_api_link/">product_api_link</a><br />
<a href="/providers/azure/api_management/product_group/">product_group</a><br />
<a href="/providers/azure/api_management/product_group_link/">product_group_link</a><br />
<a href="/providers/azure/api_management/product_policy/">product_policy</a><br />
<a href="/providers/azure/api_management/product_subscriptions/">product_subscriptions</a><br />
<a href="/providers/azure/api_management/product_wiki/">product_wiki</a><br />
<a href="/providers/azure/api_management/product_wikis/">product_wikis</a><br />
<a href="/providers/azure/api_management/quota_by_counter_keys/">quota_by_counter_keys</a><br />
<a href="/providers/azure/api_management/quota_by_period_keys/">quota_by_period_keys</a><br />
<a href="/providers/azure/api_management/region/">region</a><br />
<a href="/providers/azure/api_management/reports/">reports</a><br />
<a href="/providers/azure/api_management/service/">service</a><br />
<a href="/providers/azure/api_management/service_domain_ownership_identifier/">service_domain_ownership_identifier</a><br />
<a href="/providers/azure/api_management/service_skus_available_service_skus/">service_skus_available_service_skus</a><br />
<a href="/providers/azure/api_management/service_sso_token/">service_sso_token</a><br />
<a href="/providers/azure/api_management/sign_in_settings/">sign_in_settings</a><br />
<a href="/providers/azure/api_management/sign_up_settings/">sign_up_settings</a><br />
<a href="/providers/azure/api_management/skus/">skus</a><br />
<a href="/providers/azure/api_management/subscription/">subscription</a><br />
<a href="/providers/azure/api_management/subscription_secrets/">subscription_secrets</a><br />
<a href="/providers/azure/api_management/tag/">tag</a><br />
<a href="/providers/azure/api_management/tag_api_link/">tag_api_link</a><br />
<a href="/providers/azure/api_management/tag_operation_link/">tag_operation_link</a><br />
<a href="/providers/azure/api_management/tag_product_link/">tag_product_link</a><br />
<a href="/providers/azure/api_management/tag_resource/">tag_resource</a><br />
<a href="/providers/azure/api_management/tenant_access/">tenant_access</a><br />
<a href="/providers/azure/api_management/tenant_access_git/">tenant_access_git</a><br />
<a href="/providers/azure/api_management/tenant_access_secrets/">tenant_access_secrets</a><br />
<a href="/providers/azure/api_management/tenant_configuration/">tenant_configuration</a><br />
<a href="/providers/azure/api_management/tenant_configuration_sync_state/">tenant_configuration_sync_state</a><br />
<a href="/providers/azure/api_management/tenant_settings/">tenant_settings</a><br />
<a href="/providers/azure/api_management/user/">user</a><br />
<a href="/providers/azure/api_management/user_confirmation_password/">user_confirmation_password</a><br />
<a href="/providers/azure/api_management/user_group/">user_group</a><br />
<a href="/providers/azure/api_management/user_identities/">user_identities</a><br />
<a href="/providers/azure/api_management/user_shared_access_token/">user_shared_access_token</a><br />
<a href="/providers/azure/api_management/user_subscription/">user_subscription</a><br />
<a href="/providers/azure/api_management/workspace/">workspace</a><br />
<a href="/providers/azure/api_management/workspace_api/">workspace_api</a><br />
<a href="/providers/azure/api_management/workspace_api_diagnostic/">workspace_api_diagnostic</a><br />
<a href="/providers/azure/api_management/workspace_api_operation/">workspace_api_operation</a><br />
<a href="/providers/azure/api_management/workspace_api_operation_policy/">workspace_api_operation_policy</a><br />
<a href="/providers/azure/api_management/workspace_api_policy/">workspace_api_policy</a><br />
<a href="/providers/azure/api_management/workspace_api_release/">workspace_api_release</a><br />
<a href="/providers/azure/api_management/workspace_api_revision/">workspace_api_revision</a><br />
<a href="/providers/azure/api_management/workspace_api_schema/">workspace_api_schema</a><br />
<a href="/providers/azure/api_management/workspace_api_version_set/">workspace_api_version_set</a><br />
<a href="/providers/azure/api_management/workspace_backend/">workspace_backend</a><br />
<a href="/providers/azure/api_management/workspace_certificate/">workspace_certificate</a><br />
<a href="/providers/azure/api_management/workspace_diagnostic/">workspace_diagnostic</a><br />
<a href="/providers/azure/api_management/workspace_global_schema/">workspace_global_schema</a><br />
<a href="/providers/azure/api_management/workspace_group/">workspace_group</a><br />
<a href="/providers/azure/api_management/workspace_group_user/">workspace_group_user</a><br />
<a href="/providers/azure/api_management/workspace_link/">workspace_link</a><br />
<a href="/providers/azure/api_management/workspace_links/">workspace_links</a><br />
<a href="/providers/azure/api_management/workspace_logger/">workspace_logger</a><br />
<a href="/providers/azure/api_management/workspace_named_value/">workspace_named_value</a><br />
<a href="/providers/azure/api_management/workspace_named_value_value/">workspace_named_value_value</a><br />
<a href="/providers/azure/api_management/workspace_notification/">workspace_notification</a><br />
<a href="/providers/azure/api_management/workspace_notification_recipient_email/">workspace_notification_recipient_email</a><br />
<a href="/providers/azure/api_management/workspace_notification_recipient_user/">workspace_notification_recipient_user</a><br />
<a href="/providers/azure/api_management/workspace_policy/">workspace_policy</a><br />
<a href="/providers/azure/api_management/workspace_policy_fragment/">workspace_policy_fragment</a><br />
<a href="/providers/azure/api_management/workspace_policy_fragment_references/">workspace_policy_fragment_references</a><br />
<a href="/providers/azure/api_management/workspace_product/">workspace_product</a><br />
<a href="/providers/azure/api_management/workspace_product_api_link/">workspace_product_api_link</a><br />
<a href="/providers/azure/api_management/workspace_product_group_link/">workspace_product_group_link</a><br />
<a href="/providers/azure/api_management/workspace_product_policy/">workspace_product_policy</a><br />
<a href="/providers/azure/api_management/workspace_subscription/">workspace_subscription</a><br />
<a href="/providers/azure/api_management/workspace_subscription_secrets/">workspace_subscription_secrets</a><br />
<a href="/providers/azure/api_management/workspace_tag/">workspace_tag</a><br />
<a href="/providers/azure/api_management/workspace_tag_api_link/">workspace_tag_api_link</a><br />
<a href="/providers/azure/api_management/workspace_tag_operation_link/">workspace_tag_operation_link</a><br />
<a href="/providers/azure/api_management/workspace_tag_product_link/">workspace_tag_product_link</a><br />
</div>
</div>
